from pathlib import Path
path = Path('.')
try:
    def total_salary(path):
        with open(path, 'r', encoding="utf-8") as file:
            salary = list()
            for line in file:        
                salary.append(line.split(',')[1])
            new_salary = salary
            new_salary = [line.rstrip() for line in new_salary] 
            new_salary_len = len(new_salary)
            total = 0  
            for line in new_salary:               
                salary_int = int(line)
                total += salary_int      
                average = total // new_salary_len
                total_salary = (total,average) 
                  
            return (total_salary)

except Exception as e:
    print(f'{e} ')
   
total,average = total_salary('text.txt')     
print (f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
