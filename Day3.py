average_score = float(input("enter your average score: "))
if average_score<49:
    print("you have failed the exam.")
else:
    if average_score>=50 and average_score<=60:
        print("you have passed the exam with grade sc pass.")
    else:
        if average_score >=70 and average_score <=89:
            print("you have passed the exam with grade with a fc.")
        else:
           if averge_score >=90 and averge_score <=100:
              print("you have passed the exam with grade with a distinction.")
           else:
               print("invalid exam score:")
               
    