import enum

def prob_1():
    while(True):
        try:
            fn = int(input("Enter the first number: "))
            sn = int(input("Enter the first number: "))
        except ValueError:
            print("Input must be a number")
            continue
        except ZeroDivisionError:
            print("Second input must not be zero")
            continue
        except Exception as e:
            print(f"Error: {e}")
            continue
        if(sn == 0):
            print("Second input must not be zero")
            continue
        break

    odd_total = 0
    even_total = 0
    all_total = 0

    for i in range(fn, sn + 1):
        all_total += i
        
        if(i % 2 == 0):
            even_total += i
            print(f"Even {i}")

        if(i % 2 != 0):
            odd_total += i
            print(f"Odd {i}")


    print(f"Total odd number: {odd_total}")
    print(f"Total even number: {even_total}")
    print(f"Total all number: {all_total}")


def prob_2():
    collectionss = [1, 2, 3, 4, 5, 6, 7]

    middle = len(collectionss) / 2

    if((middle - int(middle)) == 0):
        middle -= 1
        print(f"Corrected: {middle}")

    print(f"First: {collectionss[0]}")
    print(f"Last: {collectionss[-1]}")
    print(f"Middle: {collectionss[int(middle)]}")

def prob_3():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_list = []
    even_list = []

    for i in orig_list:
        if (i % 2 == 0):
            even_list.append(i)
        if (i % 2 != 0):
            odd_list.append(i)

    print("Even Number:")
    for i in even_list:
        print(f"\t{i}")

    print("Odd Number:")
    for i in odd_list:
        print(f"\t{i}")

def prob_4():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_list = []
    even_list = []
    i = 0

    while (i < len(orig_list)):

        if (i % 2 == 0):
            even_list.append(orig_list[i])

        if (i % 2 != 0):
            odd_list.append(orig_list[i])
            
        i += 1

    print("Even Number:")
    for i in even_list:
        print(f"\t{i}")

    print("Odd Number:")
    for i in odd_list:
        print(f"\t{i}")

def prob_5():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    i = 0

    while(i < len(orig_list)):
        print(f"Index: {i}\tData: {orig_list[i]}")
        i += 1    

def prob_6():
    orig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    i = 0

    while(i < len(orig_list)):
        print(f"\tData: {orig_list[i]}")
        i += 1    

def load_bad_words(filepath="badword.txt"):
    """Load bad words from a .txt file (one per line)."""
    with open(filepath, "r", encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]

BAD_WORDS = set(load_bad_words())

def contains_bad_words(text: str, bad_words=BAD_WORDS) -> bool:
    """Check if text contains any bad word (no regex)."""
    words = text.lower().split()
    return any(word in BAD_WORDS for word in words)

def validate(text):
    checker = contains_bad_words(text)
    return checker

def prob_7():
    my_string = "2, 2, 3, 2, 4, 1, 2, 3, 3, 3, 4, 1, 2, 3, 3, 2, 3, 4, 1, 2, 3"
    my_list = my_string.split(", ")
    empty_list = []

    for i in my_list:
        if i in empty_list:
            continue
        empty_list.append(i)

    empty_list.sort()

    for i in empty_list:
        print(i, end=", ")

def prob_8():
    my_string = "2, 2, 3, 2, 4, 1, 2, 3, 3, 3, 4, 1, 2, 3, 3, 2, 3, 4, 1, 2, 3"
    my_list = my_string.split(", ")
    
    my_set = set(my_list)
    new_list = list(my_set)
    new_list.sort()

    for i in new_list:
        print(i, end=", ")

def prob_9(digit: int):
    digit_str = str(digit)
    sum_of_all = 0
    counter = 0

    while counter < len(digit_str):
        sum_of_all += int(digit_str[counter])
        counter += 1

    print(f"Sum of all num: {sum_of_all}")

def prob_10(digit: int):
    digit_str = str(digit)
    sum_of_all = 0

    for i in digit_str:
        sum_of_all += int(i)

    print(f"Sum of all num: {sum_of_all}")

# Enum for question type
class QuestionType(enum.Enum):
    MULTIPLE_CHOICE = "multiple_choice"
    ESSAY = "essay"

type_map = {
    "multiple_choice": QuestionType.MULTIPLE_CHOICE,
    "essay": QuestionType.ESSAY
}

def handle_survey_input_exists(svy_questions: dict) -> tuple[bool, list]:
    """Method to check if each input in the dict of questionnaire exists.

    Args:
        svy_questions (dict): Suvey questionnaire

    Returns:
        tuple (bool, list): Returns a flag if it has a missing ouput and a message to indicate which is missing from each question
    """

    qflag = []
    each_qcheck = []

    for qcounter, (qkey, qvalue) in enumerate(svy_questions.items(), start=1):
        result = {}
        each_qdata = []
        q_type = type_map.get(qvalue.get("type", "").lower(), "")

        if not qkey:
            result[f"Question{qcounter}"] = False
            each_qdata.append(True)

        if not qvalue.get("questionNum"):
            result["questionNum"] = False
            each_qdata.append(True)

        if not qvalue.get("type"):
            result["type"]= False
            each_qdata.append(True)

        if q_type == QuestionType.MULTIPLE_CHOICE:
            if not qvalue.get("choice"):
                result["choice"] = False
                each_qdata.append(True)

        if not qvalue.get("answer"):
            result["answer"] = False
            each_qdata.append(True)

        if result:
            qflag.append({f"Question {qcounter}": result})

        each_qcheck.append(any(each_qdata))
        qcounter +=1

    return any(each_qcheck), qflag

# ✅ All valid questions
svy_questions_valid = {
    "q1": {
        "questionNum": 1,
        "type": "multiple_choice",
        "choice": ["A", "B", "C"],
        "answer": "A"
    },
    "q2": {
        "questionNum": 2,
        "type": "essay",
        "answer": "This is my essay."
    }
}

# ❌ Missing type, no answer
svy_questions_missing_type = {
    "q1": {
        "questionNum": 1,
        "choice": ["Yes", "No"],
        "answer": ""
    }
}

# ❌ Multiple choice but no choices
svy_questions_missing_choices = {
    "q1": {
        "questionNum": 1,
        "type": "multiple_choice",
        "choice": [],
        "answer": "Yes"
    }
}

# ❌ Missing questionNum, empty answer
svy_questions_missing_qnum_answer = {
    "q1": {
        "type": "essay",
        "answer": ""
    }
}

# ❌ Mixed valid + invalid
svy_questions_mixed = {
    "q1": {
        "questionNum": 1,
        "type": "multiple_choice",
        "choice": [],
        "answer": ""
    },
    "q2": {
        "questionNum": 2,
        "type": "essay",
        "answer": "My response."
    },
    "": {  # ❌ empty key
        "questionNum": 3,
        "type": "essay",
        "answer": ""
    }
}

survey_data = {
    "q1": {
        "questionNum": 1,
        "type": "multiple_choice",
        "choice": ["A", "B", "C"],
        "answer": "A"
    },
    "q2": {  # missing type
        "questionNum": 2,
        "choice": ["Yes", "No"],
        "answer": "Yes"
    },
    "q3": {  # missing choice
        "questionNum": 3,
        "type": "multiple_choice",
        "answer": "B"
    },
    "q4": {  # missing answer
        "questionNum": 4,
        "type": "essay"
    },
    "": {  # empty key, missing everything
    }
}

survey_data_2 = {
    "q1": {
        "questionNum": 1,
        "type": "multiple_choice",
        "choice": ["A", "B", "C"],
        "answer": "A"
    },
    "q2": {
        "questionNum": 2,
        "type": "essay",
        "answer": "This is an essay answer."
    },
    "q3": {
        "questionNum": 3,
        "type": "multiple_choice",
        "choice": ["Yes", "No"],
        "answer": "Yes"
    }
}

test_list = [svy_questions_valid, svy_questions_missing_type, svy_questions_missing_choices, svy_questions_missing_qnum_answer,svy_questions_mixed]

'''
for i in test_list:
    test_valid_list = handle_survey_input_exists(i)
    for y in test_valid_list:
        print(y)
    print()
'''

flagging, test_list_2 = handle_survey_input_exists(survey_data_2)
print(flagging)
if flagging:
    for i in test_list_2:
        print(i)
