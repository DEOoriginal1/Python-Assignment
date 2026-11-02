student_result = [("Alice", 78), ("Bob", 45), ("Charlie", 90), ("Diana", 62), ("Kent", 30)]



for student_name, student_scores in student_result:
       print(f"""Name: ", {student_name}
            "Score: ", {student_scores}""")
      
for student_name, student_scores in student_result:
      if student_scores >= 50:
            print(f"""Name: ", {student_name}
                "Score: ", {student_scores}""")
            
counter = 0
for student_name, student_scores in student_result:
      if student_scores >= 50:
            counter += 1

print("Student passed: ", counter)


