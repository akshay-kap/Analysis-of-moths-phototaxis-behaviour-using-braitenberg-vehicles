from controller import Robot, DistanceSensor, Motor, LightSensor,GPS

# time in [ms] of a simulation step
TIME_STEP = 64
RANGE = 512

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()
l = robot.getGPS("gps")
l.enable(TIME_STEP)
ps =[]
psNames = [ 'ds0', 'ds1', 'ds2', 'ds7','ds3', 'ds4', 'ds5', 'ds6']
ls = []
lsNames = ['ls0', 'ls1', 'ls2', 'ls7',
           'ls3', 'ls4', 'ls5', 'ls6']

   
for i in range(8):
     ls.append(robot.getLightSensor(lsNames[i]))
     ls[i].enable(TIME_STEP)
     ps.append(robot.getDistanceSensor(psNames[i]))
     ps[i].enable(TIME_STEP)

leftMotor = robot.getMotor('left wheel motor')
rightMotor = robot.getMotor('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)
list_x_z = []

# feedback loop: step simulation until receiving an exit event
while robot.step(TIME_STEP) != -1:
    
    # read sensors outputs
    psValues = []
    lsValues = []
    for i in range(8):
        lsValues.append(ls[i].getValue())
        psValues.append(ps[i].getValue())
        w = l.getValues() 
        print("X coordinate is :",w[0], "Z coordinate is :",w[2]) 
        a = w[0]
        b = w[2]
        list_ab = [a,b]
        list_x_z.append(list_ab)
        #if(a**2+b**2 <=0.04):
         #   print("The agent reached the minimum distance")
            
    with open('A3 I1 S1 C4 plus1.txt', 'w') as filehandle:
        filehandle.writelines("%s\n" % place for place in list_x_z)
   
    # initialize motor speeds at 50% of MAX_SPEED.
    leftSpeed  = 0.2 * MAX_SPEED
    rightSpeed = 0.2 * MAX_SPEED
    a = 1
    
    
    leftSpeed = leftSpeed + a*(1- (lsValues[4]/RANGE)) + a*(1- (lsValues[5]/RANGE)) + a*(1- (lsValues[6]/RANGE)) + 10*(1- (lsValues[7]/RANGE))
    rightSpeed = rightSpeed + a*(1- (lsValues[0]/RANGE)) + a*(1- (lsValues[1]/RANGE)) + a*(1- (lsValues[2]/RANGE)) + (1- (lsValues[3]/RANGE))
    c = 4
    
    leftSpeed  = leftSpeed + c*psValues[0]/RANGE + c*psValues[1]/RANGE + c*psValues[2]/RANGE + c*psValues[3]/RANGE
    rightSpeed = rightSpeed + c*psValues[4]/RANGE + c*psValues[5]/RANGE + c*psValues[6]/RANGE + c*psValues[7]/RANGE
    

    # write actuators inputs
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)