import pgzrun

WIDTH=870
HEIGHT=650
TITLE="QUIZ MASTER"

question_box=Rect(0,0,650,150)
answer_box1=Rect(0,0,300,150)
answer_box2=Rect(0,0,300,150)
answer_box3=Rect(0,0,300,150)
answer_box4=Rect(0,0,300,150)
skip_box=Rect(0,0,150,330)
score_box=Rect(0,0,150,50)
timer_box=Rect(0,0,150,150)
marquee_box=Rect(0,0,880,80)

question_box.move_ip(20,100)
answer_box1.move_ip(20,270)
answer_box2.move_ip(370,270)
answer_box3.move_ip(20,450)
answer_box4.move_ip(370,450)
skip_box.move_ip(700,270)
score_box.move_ip(700,50)
timer_box.move_ip(700,100)
marquee_box.move_ip(0,0)

is_game_over=False
score=0
time_left=10
question_file="questions.txt"
marquee_msg=""

answer_boxes=[answer_box1, answer_box2, answer_box3, answer_box4]
questions=[]
question_count=0
question_index=0

def draw():
    global marquee_msg

    screen.clear()
    screen.fill("black")

    screen.draw.filled_rect(question_box, "#AD91A3")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(skip_box, "#9D91A3")
    screen.draw.filled_rect(timer_box, "#C49792")
    screen.draw.filled_rect(score_box, "#C49792")


    for answer_box in answer_boxes:
        screen.draw.filled_rect(answer_box, "#5D5179")

    
    marquee_msg=f"Welcome to the Quiz Master Game!You are on question {question_index}/{question_count}"

    screen.draw.textbox(marquee_msg, marquee_box, color="white")

    screen.draw.textbox(str(time_left), timer_box, color="#854D27", shadow=(0.5,0.5), scolor="grey")

    screen.draw.textbox("Skip", skip_box, color="black", angle=-90)
    
    screen.draw.textbox(f"Score:{score}", score_box, color="#854D27")

    screen.draw.textbox("hello world!", question_box, color="purple", shadow=(0.5,0.5), scolor="grey")



def update():
    pass

pgzrun.go()