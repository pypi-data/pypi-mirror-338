from typing import Any, Dict, List, Optional, Union

import yaml  # Keep import here as it's specific to this function

from dq_tools.core import DataQuality

# Type alias for the connection object
Connection = Any


def run_checks_from_yaml(
    con: Connection, yaml_path: str, return_dq: bool = False
) -> Optional[DataQuality]:
    """
    Runs data quality checks defined in a YAML file.

    Args:
        con: Database connection object.
        yaml_path: Path to the YAML configuration file.
        return_dq: If True, returns the DataQuality instance.

    Returns:
        Optional[DataQuality]: The DataQuality instance if return_dq is True, else None.
    """
    try:
        with open(yaml_path, "r") as f:
            # Type hint for loaded YAML structure (can be complex)
            checks_config: Dict[str, List[Union[str, Dict[str, Any]]]] = yaml.safe_load(
                f
            )
            if not isinstance(checks_config, dict):
                print(f"Error: YAML content in {yaml_path} is not a dictionary.")
                return None
    except FileNotFoundError:
        print(f"Error: YAML file not found at {yaml_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file {yaml_path}: {e}")
        return None

    dq = DataQuality(con)

    for section, checks in checks_config.items():
        if not isinstance(section, str) or not section.startswith("checks for "):
            dq.results.append(
                {  # type: ignore[typeddict-item] # Allow adding 'error' key
                    "table": "unknown",
                    "description": f"Section invalide : {section}",
                    "success": False,
                    "error": "Format non reconnu",
                }
            )
            continue

        table: str = section.split("checks for ")[1].strip()

        if not isinstance(checks, list):
            dq.results.append(
                {  # type: ignore[typeddict-item]
                    "table": table,
                    "description": (
                        f"Checks for section '{section}' should be a list, "
                        f"got {type(checks).__name__}"
                    ),
                    "success": False,
                    "error": "Format non reconnu",
                }
            )
            continue

        for check in checks:
            if isinstance(check, str):
                if ":" in check:
                    check_type, arg_str = map(str.strip, check.split(":", 1))
                    # Attempt to parse arg_str if it looks like a number,
                    # otherwise treat as string
                    try:
                        arg: Any = int(arg_str)
                    except ValueError:
                        try:
                            arg = float(arg_str)
                        except ValueError:
                            arg = arg_str  # Keep as string if not number

                    dq.run_check(table, check_type, arg)
                else:
                    # Handle simple check types without arguments if needed,
                    # or mark as error
                    dq.results.append(
                        {  # type: ignore[typeddict-item]
                            "table": table,
                            "description": f"Format invalide (manque ':'?) : {check}",
                            "success": False,
                            "error": "Format invalide",
                        }
                    )

            elif isinstance(check, dict):
                for check_type, args in check.items():
                    if isinstance(args, dict):
                        dq.run_check(table, check_type, **args)
                    else:
                        # Pass single non-dict argument as positional arg
                        dq.run_check(table, check_type, args)

            else:
                dq.results.append(
                    {  # type: ignore[typeddict-item]
                        "table": table,
                        "description": (
                            f"Type de check non pris en charge : "
                            f"{type(check).__name__}"
                        ),
                        "success": False,
                        "error": "Type non supporté",
                    }
                )

    dq.report()
    if return_dq:
        return dq
    return None  # Explicitly return None if return_dq is False
