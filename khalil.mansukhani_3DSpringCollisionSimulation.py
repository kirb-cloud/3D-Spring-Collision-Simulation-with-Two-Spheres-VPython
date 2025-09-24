from vpython import *
#Web VPython 3.2

scene = canvas(background = color.white)
L_eq = 1 # spring equlibrium length
k = 15    #spring constant
#μ = 0.1 #friction coefficient 

ground = box(pos = vec(0, -0.05, 0), size = vec(7, 0.02, 0.4), color = color.green)

# Set up TWO sphere objects
ball = sphere(pos = vec(-2.5, 0, 0), radius = 0.05, mass = 1, v = vec(1, 0, 0),
    make_trail = True, color = color.blue)
    
rock = sphere(pos = vec(3, 0, 0), radius = 0.05, mass = 0.5, v = vec(-0.5, 0, 0),
    make_trail = True, color = color.red)
    

    
    
""" TODO 1: Define initial momentum of each object """

ball.p = ball.mass * ball.v
rock.p = rock.mass * rock.v

""" TODO 6: Set up graphs and curves according to the assignent (SAVE THIS FOR THE END) """

###GRAPH 1: Plot velocity (x & y) for both rock and ball###
Vel_graph = graph(title = 'X- and Y-Velocity of Ball and Rock vs. Time (m/s)', xtitle = 't(s)', ytitle = 'Velocity (m/s)') 
ballYvelCurve = gcurve(graph = Vel_graph, color = color.red)    
ballXvelCurve = gcurve(graph = Vel_graph, color = color.blue)
rockYvelCurve = gcurve(graph = Vel_graph, color = color.green)    
rockXvelCurve = gcurve(graph = Vel_graph, color = color.orange)


###GRAPH 2: Plot inidividual momentum (x & y) for both rock and ball###
p_graph = graph(title = 'X- & Y- Momentum of Ball and Rock vs. Time (Kg * m/s)', xtitle = 't(s)', ytitle = 'Momentum (kg * m/s)')
pXballCurve = gcurve(graph = p_graph, color = color.red) 
pYballCurve = gcurve(graph = p_graph, color = color.blue) 
pXrockCurve = gcurve(graph = p_graph, color = color.green) 
pYrockCurve = gcurve(graph = p_graph, color = color.orange)


###GRAPH 3: Plot total momentum as a function of time###
p_total_graph = graph(title = 'Total Momentum of the System vs. Time (Kg * m/s)', xtitle = 't(s)', ytitle = 'Total Momentum (kg * m/s)')
pCurve = gcurve(graph = p_total_graph, color = color.cyan)


###GRAPH 4: Plot ball total energy###
t_graph_ball = graph(title = 'Total Energy of Ball vs. Time (J/s)', xtitle = 't(s)', ytitle = 'J')
keBCurve = gcurve(graph = t_graph_ball, color = color.red)    
eBSpringCurve = gcurve(graph = t_graph_ball, color = color.blue)  
teBCurve = gcurve(graph = t_graph_ball, color = color.green)


###GRAPH 5: Plot rock total energy###
t_graph_rock = graph(title = 'Total Energy of Rock vs. Time (J/s)', xtitle = 't(s)', ytitle = 'J')
keRCurve = gcurve(graph = t_graph_rock, color = color.red)    
eRSpringCurve = gcurve(graph = t_graph_rock, color = color.blue)  
teRCurve = gcurve(graph = t_graph_rock, color = color.green)


# set up time variables
t = 0
dt = 0.005

# distance and equillibrium length 
R = rock.pos - ball.pos
L = R.mag - L_eq

""" TODO 2: Calculate and print initial SYSTEM momentum and KE (BEFORE while loop starts) """
KE_ball = ball.p.mag2 / (2*ball.mass)
KE_rock = rock.p.mag2 / (2*rock.mass)

# total p and total KE
KE_sys = KE_ball + KE_rock
p_total = ball.p + rock.p

# initialize PE
U_spring_ball = 0
U_spring_rock = 0

# initialize ME 
ME_ball = KE_ball + U_spring_ball 
ME_rock = KE_rock + U_spring_rock


print(f'Initial Kinetic Energy of System: {KE_sys}')
print(f'Initial System Momentum: {p_total}')

while abs(ball.pos.x) and abs(rock.pos.x) < 3.2:
    rate(500)
    
    
    """ TODO 3: Determine whether the objects are close enough, then set forces accordingly using an if statement. THINK ABOUT BOTH CASES """
    """ Calculate spring energy SE depending on whether a force is applied or not """
 
    R = rock.pos - ball.pos
    L = R.mag - L_eq

    # force on the ball Fb
    # force on the rock Fr

    if R.mag < L_eq:
        Fb = -k * (L) * -R.hat 
        Fr = -k * (L) * R.hat 
        U_spring_ball = 1/2*k*L.mag2
        U_spring_rock = 1/2*k*L.mag2
    else:
        Fb = vec(0,0,0)
        Fr = vec(0,0,0)
    
    #friction force
    #F_friction_ball = -μ * ball.v
    #F_friction_rock = -μ * rock.v
                    
    #ball.p = ball.p + (Fb + F_friction_ball) * dt
    ball.p = ball.p + Fb * dt
    ball.v = ball.p / ball.mass
    ball.pos = ball.pos + ball.v * dt
    
    #rock.p = rock.p + (Fr + F_friction_rock) * dt
    rock.p = rock.p + Fr * dt
    rock.v = rock.p / rock.mass
    rock.pos = rock.pos + rock.v * dt
    
    # calculate total momentum 
    p_total = ball.p + rock.p
    
    """ TODO 4: Calculate the SYSTEM kinetic energy HERE """
    KE_ball = ball.p.mag2 / (2*ball.mass)
    KE_rock = rock.p.mag2 / (2*rock.mass)
    KE_sys = (KE_ball + KE_rock) 
    
    # calculate total mech energy for rock and ball (individually)
    
    ME_ball = KE_ball + U_spring_ball
    ME_rock = KE_rock + U_spring_rock 
    
    
    """ TODO 7: Plot the curves on the graphs that you set up earlier (SAVE THIS FOR THE END) """
    
   
   ###GRAPH 1: Plot velocity (x & y) for both rock and ball###
   
    ballYvelCurve.plot(t, ball.v.y)
    ballXvelCurve.plot(t, ball.v.x)
    rockYvelCurve.plot(t, rock.v.y)
    rockXvelCurve.plot(t, rock.v.x)
   
   ###GRAPH 2: Plot inidividual momentum (x & y) for both rock and ball###
    
    pXballCurve.plot(t, ball.p.x) 
    pYballCurve.plot(t, ball.p.y) 
    pXrockCurve.plot(t, rock.p.x) 
    pYrockCurve.plot(t, rock.p.y) 
       
   
   ###GRAPH 3: Plot total momentum as a function of time###
    pCurve.plot(t, p_total.mag)
   
   
   ###GRAPH 4: Plot ball total energy###
    keBCurve.plot(t, KE_ball) # KE ball
    eBSpringCurve.plot(t, U_spring_ball) # PE rock
    teBCurve.plot(t, ME_ball) 
    
    
    ###GRAPH 5: Plot rock total energy###
    keRCurve.plot(t, KE_rock) # KE rock
    eRSpringCurve.plot(t, U_spring_rock) # PE rock
    teRCurve.plot(t, ME_rock)
    
    
    # update time
    t = t + dt

""" TODO 5: Calculate and print FINAL system momentum and KE (AFTER the while loop has finished) """
# set up 2 different variables: final momentum and final kinetic energy
print(f'Final Kinetic Energy of System: {KE_sys}')
print(f'Final System Momentum: {p_total}')