def job_sequencing(jobs):
    # Sort jobs by profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    max_deadline = max(job[1] for job in jobs)
    slots = [False] * max_deadline
    result = [None] * max_deadline
    
    total_profit = 0
    
    for job in jobs:
        job_id, deadline, profit = job
        
        # Find a free slot
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if not slots[i]:
                slots[i] = True
                result[i] = job_id
                total_profit += profit
                break
    
    print("Job sequence:", result)
    print("Total profit:", total_profit)


# Example
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_sequencing(jobs)
