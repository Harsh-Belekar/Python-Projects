import turtle as t

#Adding Some Constants
starting_position=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up=90
Down=270
Left=180
Right=0

#Create Snake class
class SnakeClass:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0] #set Snake head

    #Create snake's Starting body
    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    #Create body for Snake
    def add_segment(self,position):
        new_segment=t.Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position) #Move Segment to Specific position
        self.segments.append(new_segment) #Add New segment to Segment List

    #Add tail in Snake body
    def add_tail(self):
        self.add_segment(self.segments[-1].position()) #Add new Segment to last Segment of snake 

    #Move Snake Forward
    def move(self):
        # Move Last segment to Second last and Second last to Next and Continues
        for seg_num in range(len(self.segments)-1,0,-1): #Start for loop from last of segment list
            new_x=self.segments[seg_num-1].xcor() #Get X_Coordinate Value
            new_y=self.segments[seg_num-1].ycor() #Get Y_Coordinate Value
            self.segments[seg_num].goto(new_x,new_y) #Move Segment to Specific position

        self.head.forward(move_distance) #Move First Segment or Snake Head to Forward

    #Move Snake UP
    def Up(self):
        if self.head.heading() != Down: #Prevent snake to overWrite it's body
            self.head.setheading(Up) #Change Head direction to Up

    #Move Snake Down
    def Down(self):
        if self.head.heading() != Up: #Prevent snake to overWrite it's body
            self.head.setheading(Down) #Change Head direction to Down

    #Move Snake Left
    def Left(self):
        if self.head.heading() != Right: #Prevent snake to overWrite it's body
            self.head.setheading(Left) #Change Head direction to Left

    #Move Snake Right
    def Right(self):
        if self.head.heading() != Left: #Prevent snake to overWrite it's body
            self.head.setheading(Right) #Change Head direction to Right