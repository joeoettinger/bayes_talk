# bayesinit.py 2016-05-06 11:15:49 joseph t oettinger
# purpose/description: library of functions to initialize priors and likelihoods
# archive: contact joeoettinger@gmail.com; in ~/justabs 
# comments: prior = P(H) = ph = prob of hypothesis; likellihood = P(D|H) = phgd 
# revision log
from __future__ import absolute_import, division, print_function, unicode_literals


def init_uniform_ph():
    """ From the number of hypotheses calculate their initial 
    probability  (priors).
    input: num_h, the number of hypotheses
    return value: ph, a list of num_h probabilites, each == 1/num_h 
    """
    num_h = eval(input('enter number of hypotheses '))
    ph = [1/num_h]*num_h
    return (ph)

def init_uni_ph_w_arg(num_h):
    """ From the number of hypotheses calculate their initial 
    probability  (priors).
    arg: num_h, the number of hypotheses
    return value: ph, a list of num_h probabilites, each == 1/num_h 
    """
    ph = [1/num_h]*num_h
    return (ph)


def init_percent_ph():
    """ Assigns a probability of randomly slecting each of 101 hypotheses 
    in the list ph. That's 1/101. The reason it's 101 hypotheses, not 100 is
    this: The hypotheses are that the bias of a coin is such that flipping it
    will produce no heads (0%) through all heads (100%). That's 101 hypotheses.
    """
    num_h = 101
    ph = [1/num_h]*num_h
    return ph

def init_ca_ph():
    """ Set the  probability of the two hypotheses: pt has or doesn't have br CA
    from some historical data.
    """
    num_h = 2
    ph = [0]*num_h    
    ph[0] = .008
    ph[1] = .992
    return ph
    # pos mam given pt has br CA

#def calc_p_h_inv_of_size(h):
def init_ph_inv_of_size(h):
    """ Set the  probabilities of a list of hypotheses re size of a set.
    Eg number of sides on a die or number of locomotives a company owns.
    """
    raw_ph = [0] * (len(h)+1)
    for i in range(1,len(h)+1):
        raw_ph[i] = 1/(i) 
    sum_raw_ph = sum(raw_ph)
    ph = [0]*len(h)
    for i in range(1,len(h)):
        ph[i] = raw_ph[i]/sum_raw_ph
    print('sum(p_h) ', sum(ph))
    return ph

def init_count_pdgh(ph):
    """ From the hypothesis list and input the number of possible  successes 
    and possible failures, calculate the prob of data given hypothesis (pdgh).
    (For small number of hypotheses, could just calc the % successes and write
    a phgd list of them.)
    """ 
    num_h = len(ph)
    successes_in_h = [0]*num_h
    failures_in_h = [0]*num_h
    for i in range(0,num_h):
        print('enter number of possible successes in h[%d]' % i)
        successes_in_h[i] = eval(input())
        print('enter number of possible failures in h[%d]' % i)
        failures_in_h[i] = eval(input())

    pdgh=[0]*num_h
    for i in range(0,num_h):
        pdgh[i] = successes_in_h[i]/(successes_in_h[i] + failures_in_h[i])
    return pdgh

def init_percent_pdgh(ph):
    """ Assign the probability of getting heads (the data) to each hypothesis.
    
    """
    num_h = len(ph)
    pdgh = [0]*num_h
    for i in range(0,num_h):
        pdgh[i] = i/100
    return pdgh

def init_emptydoor_pdgh(ph):
    """ For each of the doors, set the probability that Monty will open it and
    show that it's empty.
    """
    num_h = len(ph)
    # Create the 3 member array.
    pdgh = [0]*num_h

    # If car is behind door0, prob monty will pick door1 or door2 at random;
    # so 50% chance he'll pick door1; so prob of datum (you picked door0 and door 1 is shown to 
    # be empty) given the hypothesis h[0] "car's behind door0" == 1/2
    pdgh[0] = 1/2

    # If car is _behind_ door1 (h[1]), the prob monty will _pick_ door1 
    # to show it's empty is 0.
    pdgh[1] = 0

    # If car is behind door2, prob monty will pick door1 (his only option
    # since you picked door0) and show it's empty is 1.
    pdgh[2] = 1
    return pdgh

def init_ca_pdgh():
    """ Set the  probability of the two outcome of the mammogram: positive or
    negative from some historical data.
    """

    num_h = 2
    pdgh = [0]*num_h
    pdgh[0] = .90
    pdgh[1] = .07
    return pdgh 
         
def init_dice_pdgh(h,datum):
    """ Calculate the likelihood distribution, probability of datum given
    the hypothesis pdgh, P(D|H). Each hypothesis is that one one of the 5
    regular polyhedra has been chosen.
    arguments are h, the hypothesis list the number of sides for each of the
    regular polyhedra); and datum, the number of the die that is face up.
    return value is the list (pdgh), which contains the probability of
    seeing the datum for each member of the hypothesis list.
    """
    num_h = len(h)
    pdgh = [0]*num_h
    for i in range (0, num_h):
        if datum > h[i]:
            pdgh[i] = 0
        else:
            pdgh[i] = 1/h[i]
    return pdgh

def calc_pdgh_t_ph(pdgh, ph):
    """ calculate a list (distro) of the probabilities of hypotheses given a
    datum, h_h_g_d ie P(H|D) (eg an outcome of a throw of the die or a number 
    seen on a locomotive). But the list
    is not normalized - it's "raw". Another function normalizes the list.
    Arguments are pdgh and ph, which are lists of the same length - which
    is the number of hypotheses (5 regular polyhedra).
    Return value is pdgh_t_ph, the list of un-normalized P(H|D).
    """ 
    num_h = len(ph)
    pdgh_t_ph = [0]*num_h
    # for each hypothesis
    for i in range (0, num_h):
        pdgh_t_ph[i] = pdgh[i] * ph[i] 
    return pdgh_t_ph

def init_loco_pdgh(h,datum):
    """ Calculate the likelihood distribution, probability of datum given
    the hypothesis pdgh, P(D|H). Each hypothesis is that one one of the 5
    regular polyhedra has been chosen.
    arguments are h, the hypothesis list the number of sides for each of the
    regular polyhedra); and datum, the number of the die that is face up.
    return value is the list (pdgh), which contains the probability of
    seeing the datum for each member of the hypothesis list.
    """
    print("len(h) ", len(h))
    num_h = len(h)
    pdgh = [0]*num_h
    for i in range (1, num_h):
        if datum > h[i]:
            pdgh[i] = 0
        else:
            pdgh[i] = 1/h[i]
    return pdgh

def calc_pdgh_from_counts(ph, poss_successes_in_h, poss_failures_in_h):
    """ From the hypothesis list and the number of possible  successes and
    possible failures given each hpothesis, calculate the prob of data given
    hypothesis (pdgh).
    """ 
    num_h = len(ph)
    pdgh=[0]*num_h
    for i in range(0,num_h):
        pdgh[i] = poss_successes_in_h[i]/(poss_successes_in_h[i] + poss_failures_in_h[i])
    return pdgh


#if __name__ == '__main__':
#    main(*sys.argv)
