import yaml
from dq_tools.core import DataQuality

def run_checks_from_yaml(con, yaml_path):
    with open(yaml_path, "r") as f:
        checks_config = yaml.safe_load(f)

    dq = DataQuality(con)

    for section, checks in checks_config.items():
        if not section.startswith("checks for "):
            print(f"⚠️  Section ignorée : {section}")
            continue

        table = section.split("checks for ")[1].strip()

        for check in checks:
            if isinstance(check, str):
                # Format court : "no_nulls: c_name"
                if ":" in check:
                    check_type, arg = map(str.strip, check.split(":", 1))
                    dq.run_check(table, check_type, arg)
                else:
                    print(f"❌ Format invalide : {check}")

            elif isinstance(check, dict):
                # Format long : {check_type: {...}} ou {check_type: "arg"}
                for check_type, args in check.items():
                    if isinstance(args, dict):
                        dq.run_check(table, check_type, **args)
                    else:
                        dq.run_check(table, check_type, args)

            else:
                print(f"❌ Type de check non pris en charge : {check}")

    dq.report()
