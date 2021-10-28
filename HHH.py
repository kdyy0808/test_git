#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os

file_name_r="students.txt"
file_name_w="report.txt"

score_board_dict =dict() 


def get_total_score(midterm_score,final_score):
    total_score = 0.5*float(midterm_score) + 0.5*float(final_score)
    if total_score >= 90:
        total_result = "A"
    elif total_score >= 80:
        total_result = "B"
    elif total_score >= 70:
        total_result = "C"
    elif total_score >= 60:
        total_result = "D"
    else:
        total_result = "F"
    return str(total_score)+"({}".format(total_result)+")"

def get_rank(score):
    if score >= 90:
        total_result = "A"
    elif score >= 80:
        total_result = "B"
    elif score >= 70:
        total_result = "C"
    elif score >= 60:
        total_result = "D"
    else:
        total_result = "F"
    return total_result

def show_result():

#     score_board_dict
    print("Student\t"+"Name".rjust(10)+"\tMidterm \tFinal \tFinal \tAverage \tGrade") 
    print("{}\t {}\t {}\t{}\t{}\t{}\n".format(stu_id,stu_name,stu_mid, stu_fin,stu_mean,stu_grade))

def command_waiting():
    command_input=input("#")
    if command_input == "show":
        show_result()
    else:
        print("error")



def main():
    

    if os.path.exists(file_name_r):
        with open(file_name_r,"r") as f:
            while True:
                line = f.readline()
                if line =="":
                    break
                line_list = line.split()
                if line_list[0] not in score_board_dict.keys():
                    mean_score = 0.5*(int(line_list[3])+int(line_list[4]))
                    score_board_dict[line_list[0]] = (line_list[1] +" "+ line_list[2], line_list[3],line_list[4],mean_score ,get_rank(mean_score))
    print(score_board_dict)
    score_board_keys=list(score_board_dict.keys())



    with open(file_name_w,"w") as f:
        for stu_num in range(len(score_board_dict)):
            stu_id = score_board_keys[stu_num]
            stu_name, stu_mid, stu_fin,stu_mean,stu_grade = score_board_dict[score_board_keys[stu_num]]
            f.write("{}\t {}\t {}\t{}\t{}\t{}\n".format(stu_id,stu_name,stu_mid, stu_fin,stu_mean,stu_grade))
    #         print("{} {} {}\t{}".format(stu_id,stu_mid, stu_fin,stu_total))
    print("Student\t"+"Name".rjust(10)+"\tMidterm \tFinal \tFinal \tAverage \tGrade")
    command_waiting()

if __name__ == '__main__' :
    main()


# In[ ]:




