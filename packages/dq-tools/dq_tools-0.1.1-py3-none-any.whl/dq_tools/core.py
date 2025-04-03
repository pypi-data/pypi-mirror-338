from dq_tools.builtins import BUILTIN_CHECKS

class DataQuality:
    def __init__(self, connection):
        self.con = connection
        self.results = []

    def run_check(self, table, check_type, *args, **kwargs):
        if check_type in BUILTIN_CHECKS:
            success, description, details = BUILTIN_CHECKS[check_type](self.con, table, *args, **kwargs)
            self.results.append({
                "table": table,
                "description": description,
                "success": success,
                **details
            })
        else:
            raise ValueError(f"Check type '{check_type}' is not supported.")

    def report(self):
        print("\n=== Résultat des validations ===")
        for r in self.results:
            status = "✅" if r["success"] else "❌"
            print(f"{status} {r['table']}: {r['description']}")
            if not r["success"]:
                print(f"   🔍 Détails: {r.get('details')}")

