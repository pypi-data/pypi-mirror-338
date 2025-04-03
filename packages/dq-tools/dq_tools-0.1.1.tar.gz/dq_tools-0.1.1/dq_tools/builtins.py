def expect_no_nulls(con, table, column):
    query = f"SELECT COUNT(*) FROM {table} WHERE {column} IS NULL"
    count = con.execute(query).fetchone()[0]
    return (
        count == 0,
        f"No NULLs in {column}",
        {"failures": count}
    )

def expect_row_count_greater_than(con, table, threshold):
    query = f"SELECT COUNT(*) FROM {table}"
    count = con.execute(query).fetchone()[0]
    return (
        count > threshold,
        f"Row count > {threshold}",
        {"row_count": count}
    )

def expect_column_values_in_set(con, table, column, values):
    values_str = ", ".join(f"'{v}'" for v in values)
    query = f"SELECT COUNT(*) FROM {table} WHERE {column} NOT IN ({values_str})"
    count = con.execute(query).fetchone()[0]
    return (
        count == 0,
        f"Values in set {values} for column {column}",
        {"unexpected_values": count}
    )

def expect_column_mean_between(con, table, column, min_value, max_value):
    query = f"SELECT AVG({column}) FROM {table}"
    avg = con.execute(query).fetchone()[0]
    success = min_value <= avg <= max_value
    return (
        success,
        f"Mean of {column} between {min_value} and {max_value}",
        {"actual_mean": avg}
    )

def expect_unique_column(con, table, column):
    query = f"""
    SELECT COUNT(*) - COUNT(DISTINCT {column})
    FROM {table}
    """
    duplicates = con.execute(query).fetchone()[0]
    return (
        duplicates == 0,
        f"Column {column} is unique",
        {"duplicate_count": duplicates}
    )

def expect_table_exists(con, table):
    query = f"SELECT COUNT(*) FROM information_schema.tables WHERE table_name = '{table.lower()}'"
    exists = con.execute(query).fetchone()[0] == 1
    return (
        exists,
        f"Table {table} exists",
        {"exists": exists}
    )

def expect_column_min_greater_than(con, table, column, min_value):
    query = f"SELECT MIN({column}) FROM {table}"
    value = con.execute(query).fetchone()[0]
    success = value > min_value
    return (
        success,
        f"Min of column {column} > {min_value}",
        {"actual_min": value}
    )

def expect_column_max_less_than(con, table, column, max_value):
    query = f"SELECT MAX({column}) FROM {table}"
    value = con.execute(query).fetchone()[0]
    success = value < max_value
    return (
        success,
        f"Max of column {column} < {max_value}",
        {"actual_max": value}
    )




BUILTIN_CHECKS = {
    "no_nulls": expect_no_nulls,
    "row_count_greater_than": expect_row_count_greater_than,
    "column_values_in_set": expect_column_values_in_set,
    "column_mean_between": expect_column_mean_between,
    "unique_column": expect_unique_column,
    "table_exists": expect_table_exists,
    "column_min_greater_than": expect_column_min_greater_than,
    "column_max_less_than": expect_column_max_less_than,
}
