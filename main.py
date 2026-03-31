import requests
import csv

api_url = "https://remoteok.com/api"

def load_data(api_url):
    """
    Fetches job data from the API and handles connection errors.
    """
    try:
        response = requests.get(api_url)
        return response.json()
    except:
        print("Error: Could not connect to the API. Please check your internet.")
        # Return an empty list if it fails, so the rest of the code doesn't crash!
        return []
    
    

catch_data = load_data(api_url)
print(catch_data)


# print(response.status_code)

jobs_data = catch_data
# print(type(jobs_data))
# print(len(jobs_data))

# print(jobs_data[1])

real_jobs = jobs_data[1:]

# for job in real_jobs:
#     job_title = job["position"]
#     if "Engineer" in job_title:
#         print(job["company"])
#         print(job["position"])
        
        
#list comprehension
engineer_jobs = [job for job in real_jobs if "Engineer" in job["position"]]
# print(engineer_jobs)


raw_salary = "$150,000"
cleaned_salary = raw_salary.replace("$", "").replace(",", "")
salary_int = int(cleaned_salary)
# print(type(salary_int))






messy_range = "$80k - $100k"
parts = messy_range.split("-")
print(parts)

preety_range = parts[0].replace("$", "").replace("k", "000")
int_preety_range = int(preety_range)

preety_range2 = parts[1].replace("$", "").replace("k", "000")
int_preety_range2 = int(preety_range2)

clean_salary = [int_preety_range, int_preety_range2]
print(clean_salary)



def export_to_csv(engineering_jobs, filename="engineering_jobs.csv"):
    with open (filename, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Company", "Position", "Min Salary", "Max Salary"])
        for job in engineering_jobs:
            writer.writerow([job["company"], job["position"], job["salary_min"], job["salary_max"]])
            
export_to_csv(engineer_jobs)




total_salary = 0
for job in engineer_jobs:
    total_salary += job["salary_min"]
    
lengthOfEngineerJobs = len(engineer_jobs)

final_salary = total_salary/lengthOfEngineerJobs

print(final_salary)



