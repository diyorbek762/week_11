def print_document(users_db, printer_config, user_id, printer_type, pages):
    if user_id not in users_db:
        raise KeyError("User unknown")
    if printer_type not in printer_config:
        raise KeyError("Invalid printer type")
    if pages<1 or type(pages)!=int:
        raise ValueError("Page count must be positive integer")
    cost_per_page=printer_config[printer_type]["cost"]
    total_cost=pages * cost_per_page
    if users_db[user_id]["role"]=="Staff":
        total_cost=0
    if users_db[user_id]["quota"]<total_cost:
        raise ValueError("Insufficient quota")
    users_db[user_id]["quota"]=users_db[user_id]["quota"]-total_cost
    return total_cost

def process_print_queue(users_db, printer_config, job_list):
    total_credits_burned=0.0
    jobs_failed=0
    for job in job_list:
        user_id, printer_type, pages= job
        try:
            total_cost=print_document(users_db, printer_config, user_id, printer_type, pages)
            total_credits_burned+=total_cost
        except KeyError as e:
            print(f"Print Error for {user_id}: {e}")
            jobs_failed+=1
        except ValueError as e:
            print(f"Print Error for {user_id}: {e}")
            jobs_failed+=1
    return {'total_credits_burned': total_credits_burned, 'failed_jobs': jobs_failed}

printers = {
    "BW":    {"cost": 0.10},
    "Color": {"cost": 0.50}
}

# Format: {ID: {"quota": float, "role": str}}
users = {
    "U1": {"quota": 2.00, "role": "Student"},
    "U2": {"quota": 5.00, "role": "Staff"}    # Prints for free
}

jobs = [
    ("U1", "BW", 10),      # Valid. Cost: 1.00. Rem: 1.00.
    ("U2", "Color", 20),   # Valid. Cost: 0.00 (Staff). Rem: 5.00.
    ("U1", "Color", 10),   # Error: Cost 5.00 > 1.00.
    ("U9", "BW", 1),       # Error: User unknown.
    ("U1", "3D", 1),       # Error: Invalid printer type.
    ("U1", "BW", 0)        # Error: Page count must be positive integer.
]

print(process_print_queue(users, printers, jobs))
    