from tkinter import *

def analyze():
    name = name_entry.get()

    subjects = [
        (subject1.get(), mark1.get()),
        (subject2.get(), mark2.get()),
        (subject3.get(), mark3.get()),
        (subject4.get(), mark4.get()),
        (subject5.get(), mark5.get())
    ]

    total = 0
    count = 0
    details = ""

    for subject, mark in subjects:
        if subject.strip() != "" and mark.strip() != "":
            try:
                mark = int(mark)
                total += mark
                count += 1
                details += f"{subject} : {mark}\n"
            except ValueError:
                pass

    if count == 0:
        result.config(
            text="Please enter at least one subject and marks!",
            fg="red"
        )
        return

    percentage = total / count

    if percentage >= 90:
        grade = "A+ 🌟"
    elif percentage >= 80:
        grade = "A 🎉"
    elif percentage >= 70:
        grade = "B 👍"
    elif percentage >= 60:
        grade = "C 😊"
    elif percentage >= 50:
        grade = "D 🙂"
    else:
        grade = "F 😔"

    result_text = f"""
Student Name : {name}

Subjects Entered : {count}

{details}

Total Marks : {total}
Percentage : {percentage:.2f}%
Grade : {grade}
"""

    result.config(text=result_text, fg="darkblue")


root = Tk()
root.title("Student Marks Analyzer")
root.geometry("600x700")
root.configure(bg="#E6E6FA")

Label(
    root,
    text="🎓 STUDENT MARKS ANALYZER",
    font=("Arial", 20, "bold"),
    bg="#E6E6FA",
    fg="#6A0DAD"
).pack(pady=15)

Label(
    root,
    text="Student Name",
    font=("Arial", 12, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
).pack()

name_entry = Entry(root, width=30, font=("Arial", 12))
name_entry.pack(pady=8)

frame = Frame(root, bg="#E6E6FA")
frame.pack(pady=10)

Label(
    frame,
    text="Subject Name",
    width=22,
    font=("Arial", 11, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
).grid(row=0, column=0)

Label(
    frame,
    text="Marks",
    width=10,
    font=("Arial", 11, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
).grid(row=0, column=1)

subject1 = Entry(frame, width=25)
mark1 = Entry(frame, width=10)
subject1.grid(row=1, column=0, padx=5, pady=5)
mark1.grid(row=1, column=1)

subject2 = Entry(frame, width=25)
mark2 = Entry(frame, width=10)
subject2.grid(row=2, column=0, padx=5, pady=5)
mark2.grid(row=2, column=1)

subject3 = Entry(frame, width=25)
mark3 = Entry(frame, width=10)
subject3.grid(row=3, column=0, padx=5, pady=5)
mark3.grid(row=3, column=1)

subject4 = Entry(frame, width=25)
mark4 = Entry(frame, width=10)
subject4.grid(row=4, column=0, padx=5, pady=5)
mark4.grid(row=4, column=1)

subject5 = Entry(frame, width=25)
mark5 = Entry(frame, width=10)
subject5.grid(row=5, column=0, padx=5, pady=5)
mark5.grid(row=5, column=1)

Button(
    root,
    text="ANALYZE RESULT",
    command=analyze,
    bg="#9370DB",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18
).pack(pady=20)

result = Label(
    root,
    text="Enter details and click Analyze",
    bg="white",
    fg="black",
    font=("Arial", 11),
    justify=LEFT,
    width=45,
    height=15,
    relief=RIDGE,
    bd=3
)

result.pack(pady=15)

root.mainloop() 