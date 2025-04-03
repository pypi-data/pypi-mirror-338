from typing import Any, Callable, Dict, List, Optional, Tuple

import duckdb  # Import duckdb to catch its specific errors

# Type alias for the connection object (use Any for simplicity)
Connection = Any
# Type alias for the result tuple returned by check functions
CheckResult = Tuple[bool, str, Dict[str, Any]]
# Type alias for the signature of a check function
CheckFunction = Callable[..., CheckResult]


def expect_no_nulls(con: Connection, table: str, column: str) -> CheckResult:
    query = f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL"
    try:
        count = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    return (count == 0, f"No NULLs in {column}", {"failures": count})


def expect_row_count_greater_than(
    con: Connection, table: str, threshold: int
) -> CheckResult:
    query = f"SELECT COUNT(*) FROM {table}"
    try:
        count = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    return (count > threshold, f"Row count > {threshold}", {"row_count": count})


def expect_column_values_in_set(
    con: Connection, table: str, column: str, values: List[Any]
) -> CheckResult:
    # Use parameterized query for safety and to avoid complex string formatting
    # Create placeholders (?, ?, ?)
    placeholders = ", ".join("?" for _ in values)
    # Query counts rows where the column value is NOT in the provided list
    query = f"SELECT COUNT(*) FROM {table} WHERE {column} NOT IN ({placeholders})"
    # Pass the list of values as parameters to the execute method
    try:
        count = con.execute(query, values).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    # Note: This check might be slow on large tables without indices
    return (
        count == 0,
        f"Values in set {values} for column {column}",
        {"unexpected_values": count},
    )


def expect_column_mean_between(
    con: Connection, table: str, column: str, min_value: float, max_value: float
) -> CheckResult:
    query = f"SELECT AVG({column}) FROM {table}"
    try:
        avg = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    # Handle potential None result if table is empty or column has only NULLs
    if avg is None:
        return (
            False,
            f"Could not calculate mean for {column} (all NULLs?)",
            {"actual_mean": None},
        )
    success = min_value <= avg <= max_value
    # Consider adding tolerance for floating point comparisons if needed
    return (
        success,
        f"Mean of {column} between {min_value} and {max_value}",
        {"actual_mean": avg},
    )


def expect_unique_column(con: Connection, table: str, column: str) -> CheckResult:
    # This query counts rows where the column is not unique
    query = f"""
    SELECT COUNT(*)
    FROM (
        SELECT {column}, COUNT(*) as cnt
        FROM {table}
        WHERE {column} IS NOT NULL
        GROUP BY {column}
        HAVING COUNT(*) > 1
    ) AS duplicates
    """
    # The result is the count of *values* that are duplicated,
    # not the total count of duplicate rows
    try:
        duplicate_value_count = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    return (
        duplicate_value_count == 0,
        f"Column {column} is unique",
        {"duplicate_value_count": duplicate_value_count},
    )


def expect_table_exists(con: Connection, table: str) -> CheckResult:
    # Using lower() assumes case-insensitive table names or specific DB behavior
    # Consider parameterizing the query for safety if table names can be complex
    query = (
        f"SELECT COUNT(*) FROM information_schema.tables "
        f"WHERE table_name = '{table.lower()}'"
    )
    try:
        exists = con.execute(query).fetchone()[0] == 1
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    return (exists, f"Table {table} exists", {"exists": exists})


def expect_column_min_greater_than(
    con: Connection, table: str, column: str, min_value: float
) -> CheckResult:
    query = f"SELECT MIN({column}) FROM {table}"
    try:
        value = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    if value is None:
        return (
            False,
            f"Could not calculate min for {column} (all NULLs?)",
            {"actual_min": None},
        )
    success = value > min_value
    return (success, f"Min of column {column} > {min_value}", {"actual_min": value})


def expect_column_max_less_than(
    con: Connection, table: str, column: str, max_value: float
) -> CheckResult:
    query = f"SELECT MAX({column}) FROM {table}"
    try:
        value = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    if value is None:
        return (
            False,
            f"Could not calculate max for {column} (all NULLs?)",
            {"actual_max": None},
        )
    success = value < max_value
    return (success, f"Max of column {column} < {max_value}", {"actual_max": value})


def expect_column_value_length_between(
    con: Connection,
    table: str,
    column: str,
    min_len: int = 0,
    max_len: Optional[int] = None,
) -> CheckResult:
    """Checks if the length of string values in a column is within a specified range."""
    if max_len is None:
        condition = f"LENGTH({column}) < {min_len}"
        desc = f"Length of {column} >= {min_len}"
    else:
        condition = f"LENGTH({column}) < {min_len} OR LENGTH({column}) > {max_len}"
        desc = f"Length of {column} between {min_len} and {max_len}"

    query = f"SELECT COUNT(*) FROM {table} WHERE {condition}"
    try:
        count = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    return (count == 0, desc, {"invalid_length_count": count})


def expect_column_values_to_match_regex(
    con: Connection, table: str, column: str, regex: str
) -> CheckResult:
    """Checks if string values in a column match a given regex."""
    # Ensure the column is treated as VARCHAR for regex matching if needed
    # DuckDB's regexp_matches should work on text types.
    # Parameterize the regex pattern for safety.
    query = f"SELECT COUNT(*) FROM {table} WHERE NOT regexp_matches({column}, ?)"
    try:
        count = con.execute(query, [regex]).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    desc = f"Values in {column} match regex '{regex}'"
    return (count == 0, desc, {"non_matching_count": count})


# Dictionary mapping check names (str) to check functions (Callable)
BUILTIN_CHECKS: Dict[str, CheckFunction] = {
    "no_nulls": expect_no_nulls,
    "row_count_greater_than": expect_row_count_greater_than,
    "column_values_in_set": expect_column_values_in_set,
    "column_mean_between": expect_column_mean_between,
    "unique_column": expect_unique_column,
    "table_exists": expect_table_exists,
    "column_min_greater_than": expect_column_min_greater_than,
    "column_max_less_than": expect_column_max_less_than,
    "column_value_length_between": expect_column_value_length_between,
    "column_values_to_match_regex": expect_column_values_to_match_regex,
}

# TODO: Add more checks (e.g., date format, foreign key relationships)
# TODO: Consider adding support for custom SQL checks
# TODO: Improve error handling for SQL execution errors


def expect_column_values_to_be_valid_date(
    con: Connection, table: str, column: str, date_format: str
) -> CheckResult:
    """Checks if column values are valid dates according to the specified format."""
    # DuckDB's strptime function can be used to validate date formats
    query = f"""
    SELECT COUNT(*)
    FROM {table}
    WHERE strptime({column}, ?) IS NULL
    AND {column} IS NOT NULL  -- Exclude NULL values from the check
    """
    try:
        count = con.execute(query, [date_format]).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    desc = f"Values in {column} are valid dates with format '{date_format}'"
    return (count == 0, desc, {"invalid_date_count": count})


def expect_column_values_to_be_positive(
    con: Connection, table: str, column: str
) -> CheckResult:
    """Checks if column values are positive (greater than zero)."""
    query = f"SELECT COUNT(*) FROM {table} WHERE {column} <= 0"
    try:
        count = con.execute(query).fetchone()[0]
    except duckdb.Error as e:
        return (False, f"SQL Error: {e}", {"error": str(e)})
    desc = f"Values in {column} are positive"
    return (count == 0, desc, {"non_positive_count": count})
