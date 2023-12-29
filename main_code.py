cloud_cover=int(input("enter the cloud coverage percentage"))
temp=int(input("enter the temperature in Fahrenheit"))
print("The cloud coverage is",cloud_cover,"and the temperature is",temp)

def left_trapezium(x,alpha,beta):
    if x<alpha:
        return 1
    if alpha<x and x<=beta:
        return (beta-x)/(beta-alpha)
    else:
        return 0
    
def right_trapezium(x,alpha,beta):
    if x<alpha:
        return 0
    if alpha<x and x<=beta:
        return (x-alpha)/(beta-alpha)
    else:
        return 0

def triangle(x,a,b,c):
    return max(min((x-a)/(b-a),(c-x)/(c-b)),0)

def temp_partition(x):
    freezing=0; cool=0; warm=0; hot=0;
    
    if x>0 and x<50:
        freezing=left_trapezium(x,30,50)
    if x>30 and x<70:
        cool=triangle(x,30,50,70)
    if x>50 and x<90:
        warm=triangle(x,50,70,90)
    if x>70 and x<100:
        hot=right_trapezium(x,70,90)
    return freezing, cool, warm, hot;

def cloud_partition(x):
    sunny=0; cloudy=0; overcast=0;
    
    if x>0 and x<40:
        sunny=left_trapezium(x,20,40)
    if x>20 and x<80:
        cloudy=triangle(x,20,40,80)
    if x>80 and x<100:
        overcast=right_trapezium(x,40,80)
    return sunny, cloudy, overcast;

freezing, cool, warm, hot = temp_partition(temp)
sunny, cloudy, overcast = cloud_partition(cloud_cover)   

print("\nThe fuzzy values for the crip temperature inputs are-")
print(freezing, cool, warm, hot )
print("\nThe fuzzy values for the crip cloud_coverage inputs are-")
print(sunny, cloudy, overcast )   

fast=min(sunny,warm)
slow=min(cloudy,cool)

print("\nfast=",fast,"and slow=",slow)

def area_left_trapezium(mu,alpha,beta):
    left= beta-mu*(beta-alpha)
    return 1/2*mu*(beta+left), beta/2

def area_right_trapezium(mu,alpha,beta):
    a_right=(beta-alpha)*mu+alpha
    b_right=(1/2)*mu*((100-alpha)+ (100-a_right))
    return b_right, (100-alpha)/2 + alpha

def defuzz(fast,slow):
    area_fast=0 ; area_slow=0;
    cp_fast=0; cp_slow=0;
    
    if slow!=0:
        area_fast,cp_fast = area_right_trapezium(fast,25,75)
    if fast!=0:
        area_slow,cp_slow = area_left_trapezium(slow,25,75)
    
    numerator= fast*cp_fast+slow*cp_slow
    denominator= fast+slow
    
    if denominator==0:
        print("no rules exist to give result")
    else:
        speed=numerator/denominator
        return speed
    
final_speed=defuzz(fast,slow)

if final_speed!=0:
    print("\nThe required speed is=",final_speed,"mph")
