# pid-genetic
Pid tuning with a genetic algorithm

After the quadcopter pid thing about a month ago, I decided to try a genetic algorithm to tune the pid settings.
This implementation is hella inefficient, I assume there is a better way to do it out there. 
It doesn't always converge to the same minimum, but, hey, variety is the spice of life. 

Basically:
Creates a number of possible pid settings through mutation and crossing over, then runs them against a quadcopter simulation, rated by time to stabilize and accuracy. Top two performers get bred together, repeating the cycle. If a particular pid setting fails to converge or takes too long, it is eliminated from the gene pool. If the population faces extinction, then a new population is created.

Feel free to tinker with the values in config.py.
