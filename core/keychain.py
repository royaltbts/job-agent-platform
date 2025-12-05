import subprocess

def get_key(service_name):
    """
    Reads a password stored in macOS Keychain using the 'security' command.
    """
    try:
        result = subprocess.run(
            ["security", "find-generic-password", "-s", service_name, "-w"],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            raise ValueError(f"Keychain lookup failed for: {service_name}")
        
        return result.stdout.strip()

    except Exception as e:
        raise RuntimeError(f"Error accessing keychain for {service_name}: {e}")

