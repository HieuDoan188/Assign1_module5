"""
Task 1: TODO

 - Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” 
(Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)
 - Viết một chương trình cho phép người dùng nhập tên của một tệp. Cố gắng mở 
tệp được cung cấp để truy cập đọc:
        +  Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. 
        + Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ.
    Sử dụng try/except để thực hiện việc này (đừng chỉ sử dụng một loạt câu lệnh “if” — chúng tôi muốn chương 
    trình này càng “chung chung” càng tốt). nếu ko sẽ ko có điểm
"""
import re

def find_median(lst):
    lst = sorted(lst)
    if len(lst)%2 != 0:
        median = lst[int((len(lst)-1)/2)]
    else:
        median = (lst[int(len(lst)/2-1)] + lst[int(len(lst)/2)])/2
    return median

def read_file(file_name):
    try:
        f = open("Data Files/" + file_name + ".txt", "r")
        print("Successfully opened " +  file_name + ".txt")
        return f
    except:
        print("File cannot be found.")
        read_file()
        
def task2(contents):
    count = 0
    error_line = []
    print("**** ANALYZING ****")
    for content in contents:
        temp_data = content.rstrip("\n").split(",")
        if len(temp_data) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(content)
            count += 1
            error_line.append(content)

        else:
            check_ID = re.match("^N[0-9]{8,8}", temp_data[0])
            if check_ID == None:
                print("Invalid line of data: N# is invalid")
                print(content)
                count +=1
                error_line.append(content)

    if count == 0:
        print("No errors found!")

        
    print("**** REPORT ****")
    print("Total valid lines of data: ", len(contents) - count)
    print("Total invalid lines of data:: ", count)

    return error_line

def task3(answer_key, contents, error_line):
    answer_key = answer_key.split(",")
    for i in error_line:
        contents.remove(i)

    match = []
    for content in contents:
        student_match = 0
        # tách điểm thành 1 lst để so sánh, loại bỏ ptu xuống dòng
        content = content.rstrip("\n").split(",")
        for i in range(25):
            if content[i+1] == answer_key[i]:
                student_match += 4
            elif content[i+1] == "":
                student_match += 0
            else:
                student_match -= 1
        match.append(student_match)
    
    # in kết quả theo yêu cầu
    print("Mean (average) score: ", sum(match)/len(match))
    print("Highest score: ", max(match))
    print("Lowest score: ", min(match))
    print("Range of scores: ", max(match) - min(match))
    print("Median score: ", find_median(match))

def task4():
    pass

def main():
    # run task 1
    file_name = input("Enter a class to grade (i.e. class1 for class1.txt): ")
    f = read_file(file_name)

    # run task 2 từ file đọc được ở task 1
    contents = f.readlines() # load dữ liệu từ file được đọc theo danh sách
    error_line = task2(contents)

    # run task 3 từ đáp án đúng và nội dung và những dòng ko đúng định dạng từ task2
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    task3(answer_key, contents, error_line)

    # run task 4
    task4()


    f.close()


main()


