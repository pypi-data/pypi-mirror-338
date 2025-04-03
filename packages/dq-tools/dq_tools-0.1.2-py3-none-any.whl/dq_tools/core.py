from typing import Any, Dict, List

from dq_tools.builtins import BUILTIN_CHECKS

# Define a type alias for the result dictionary for clarity
ResultDict = Dict[str, Any]


class DataQuality:
    def __init__(self, connection: Any):  # Use Any or 'duckdb.DuckDBPyConnection'
        self.con: Any = connection
        self.results: List[ResultDict] = []

    def run_check(self, table: str, check_type: str, *args: Any, **kwargs: Any) -> None:
        if check_type in BUILTIN_CHECKS:
            # Assuming check functions return Tuple[bool, str, Dict[str, Any]]
            success, description, details = BUILTIN_CHECKS[check_type](
                self.con, table, *args, **kwargs
            )
            self.results.append(
                {
                    "table": table,
                    "description": description,
                    "success": success,
                    **details,
                }
            )
        else:
            # Consider adding a specific error type later
            raise ValueError(f"Check type '{check_type}' is not supported.")

    def report(self) -> None:
        print("\n=== Résultat des validations ===")
        for r in self.results:
            status = "✅" if r["success"] else "❌"  # Assuming 'success' is always bool
            # Assuming 'table' and 'description' are always str
            print(f"{status} {r['table']}: {r['description']}")
            if not r["success"]:
                # Show error message if present
                if "error" in r:
                    print(f"   🔍 Erreur: {r['error']}")
                # Show all other details (excluding error/table/description/success)
                details = {
                    k: v
                    for k, v in r.items()
                    if k not in {"error", "table", "description", "success"}
                }
                if details:
                    print(f"   🔍 Détails: {details}")

    def validate(self) -> bool:
        """Check if all expectations passed validation.

        Returns:
            bool: True if all checks passed, False otherwise.
                  Returns True if no checks were run.
        """
        if not self.results:
            return True  # Or False, depending on desired behavior for empty results
        return all(r["success"] for r in self.results)
