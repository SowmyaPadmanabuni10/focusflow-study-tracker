# ==========================================
# FocusFlow - Smart Study Productivity Tracker
# ==========================================

study_records = []

while True:

    print("\n========== FOCUSFLOW ==========")
    print("1. Add Study Record")
    print("2. View Study Records")
    print("3. Total Study Hours")
    print("4. Average Focus Rating")
    print("5. Most Studied Subject")
    print("6. Daily Study Goal Check")
    print("7. Save Records")
    print("8. Exit")

    user_choice = input("Enter your choice: ")

    # OPTION 1
    if user_choice == '1':

        subject_name = input("Enter Subject Name: ")

        study_hours = float(input("Enter Study Hours: "))

        focus_rating = int(input("Enter Focus Rating (1-10): "))

        study_data = {
            'subject': subject_name,
            'hours': study_hours,
            'focus': focus_rating
        }

        study_records.append(study_data)

        print("Study Record Added Successfully!")

    # OPTION 2
    elif user_choice == '2':

        if len(study_records) == 0:

            print("No Study Records Found!")

        else:

            print("\n====== STUDY RECORDS ======")

            for record in study_records:

                print("Subject :", record['subject'])
                print("Hours   :", record['hours'])
                print("Focus   :", record['focus'])
                print("---------------------------")

    # OPTION 3
    elif user_choice == '3':

        total_hours = 0

        for record in study_records:

            total_hours += record['hours']

        print("Total Study Hours :", total_hours)

    # OPTION 4
    elif user_choice == '4':

        if len(study_records) == 0:

            print("No Records Available!")

        else:

            total_focus = 0

            for record in study_records:

                total_focus += record['focus']

            average_focus = total_focus / len(study_records)

            print("Average Focus Rating :", round(average_focus, 2))

    # OPTION 5
    elif user_choice == '5':

        if len(study_records) == 0:

            print("No Records Available!")

        else:

            highest_hours = 0
            top_subject = ""

            for record in study_records:

                if record['hours'] > highest_hours:

                    highest_hours = record['hours']
                    top_subject = record['subject']

            print("Most Studied Subject :", top_subject)

    # OPTION 6
    elif user_choice == '6':

        daily_goal = 5

        total_hours = 0

        for record in study_records:

            total_hours += record['hours']

        print("Today's Total Study Hours :", total_hours)

        if total_hours >= daily_goal:

            print("Excellent! Daily Goal Achieved!")

        else:

            remaining = daily_goal - total_hours

            print("You need", remaining, "more hours to reach your goal.")

    # OPTION 7
    elif user_choice == '7':

        file = open("focusflow_records.txt", "w")

        for record in study_records:

            file.write(
                f"Subject: {record['subject']} | "
                f"Hours: {record['hours']} | "
                f"Focus Rating: {record['focus']}\n"
            )

        file.close()

        print("Records Saved Successfully!")

    # OPTION 8
    elif user_choice == '8':

        print("Thank You For Using FocusFlow!")
        break

    # INVALID OPTION
    else:

        print("Invalid Choice! Please Try Again.")
        