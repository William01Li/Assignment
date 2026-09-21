# Name: Haowei Li
#Assignment one 
#ddl is 22/09/2026 23:59pm

import turtle

#task 1
def calculator():
    print("\n Simple Calculator ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Choose operation (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation")
# task 2
def qa_bot():
    print("\n Question Answering Bot")
    question = input("Ask me something: ")

    if question == "hello":
        print("Bot: Hello! Nice to meet you.")
    elif question == "python":
        print("Bot: Python is a language.")
    elif question == "jetson":
        print("Bot: Jetson Nano is an AI computer.")
    elif question == "ai":
        print("Bot: AI means Artificial Intelligence.")
    elif question == "name":
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")
# task 3
def turtle_drawing():
    screen = turtle.Screen()
    screen.bgcolor("black") 
    screen.title("Creative Turtle Drawing")
    
    pen = turtle.Turtle()
    pen.speed(0)  # set the fastest drawing speed 
    pen.width(2)
    
    # set a color list
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    # change the length and color
    for i in range(120):
        pen.pencolor(colors[i % 6]) # swithch the colors
        pen.forward(i * 2)          
        pen.left(61)                
        
    print("the drawing is finished")
    turtle.done() 

# main function
def main():
    while True:
        print("        MAIN MENU")
        print("1. Run Simple Calculator (Task 1)")
        print("2. Run QA Bot (Task 2)")
        print("3. run Turtle Drawing (Task3)")
        print("4. Exit")
        choice = input("Please select a task (1/2/3): ")
        
        if choice == '1':
            calculator()
        elif choice == '2':
            qa_bot()
        elif choice == '3':
            turtle_drawing()
            print("turtle engine finished. exiting main menu to prevent loop errors")
            break
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")
#execution
if __name__ == "__main__":
    main()
