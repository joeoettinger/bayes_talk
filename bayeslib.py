# bayeslib.py 2016-05-10 06:48:56 joseph t oettinger
# purpose/description: library of bayes functions
# archive: contact joeoettinger@gmail.com; in ~/justabs 
# comments: 
# revision log
from __future__ import absolute_import, division, print_function, unicode_literals

import matplotlib.pyplot as plt


def success_update(ph, pdgh):
    """Update a probability distribution of a set of hypotheses given the
    occurence of (a certain binary outcome, which is called the data). The
    occurrence of that outcome can be called a success.
    parameters:
    p_h     -- list of each of the probabilities of each of the hypotheses P(H)
    (eg 'you blindly selected jar 1 to pick a cookie from' or 'the coin is
    biased, so that 90% of the time it comes up heads.')
    p_d_g_h -- a corresponding list of the probabilities of the data, ie of an 
    outcome (eg an outcome such as 'you blindly picked a chocolate cookie from
    the jar' or 'the coin came up heads') given each of the hypotheses P(D|H)
    return value:
    p_h_g_d -- corresponding list of the probabilities of the hypotheses given
    the data - the left side of Bayes equation.
    """
    num_h = len(ph)
    pdgh_t_ph = [0]*num_h
    for i in range(0, num_h):
        pdgh_t_ph[i] = (pdgh[i]) * ph[i]
    return pdgh_t_ph

def failure_update(ph, pdgh):
    """Update a probability distribution of a set of hypotheses given the
    non-occurance of (a certain binary outcome, which is called the data). This non-
    occurance of the outcome can be called a failure.
    parameters:
    p_h     -- list of each of the probabilities of each of the hypotheses P(H)
    (eg 'you blindly selected jar 1 to pick a cookie from' or 'the coin is
    biased, so that 90% of the time it comes up heads.')
    p_d_g_h -- corresponding list of the probabilities of data, ie of an 
    outcome (eg an outcome such as 'you blindly picked a chocolate cookie from
    the jar' or 'the coin came up heads') given each of the hypotheses P(D|H)
    return value:
    p_h_g_d -- corresponding list of the probabilities of the hypotheses given
    non-occurence of the data.
    The difference between this function and success_update is just that you use
    1-pdgh[i] instead of pdgh[i] - given the hypothesis h[i] the probability of
    (non-occurence of the outcome of interest) ("failure") is 1-(the probability of
    its occurence.
    """
    num_h = len(ph)
    pdgh_t_ph = [0]*num_h
    for i in range(0, num_h):
        pdgh_t_ph[i] = (1-pdgh[i]) * ph[i]
    return pdgh_t_ph

def dice_loco_update(ph, pdgh):
    """ Calculate the phgd_t_ph list using corresponding members of the pdgh
    and ph lists.
    """
    num_h = len(ph)
    pdgh_t_ph = []
    for i in range (0, num_h):
        pdgh_t_ph.append(pdgh[i]*ph[i])
    #print("pdgh_t_ph ", pdgh_t_ph)
    return(pdgh_t_ph)

 
def calc_phgd(pdgh_t_ph):
    """ Normalize the numerator pdgh_t_ph  ie P(D|H) * P(H) 
    to produce p_h_g_d ie P(H|D)
    """
    num_h = len(pdgh_t_ph)
    pd = 0
    pd = sum(pdgh_t_ph)
    phgd = [0]*num_h
    for i in range(0, num_h): 
        phgd[i] = pdgh_t_ph[i]/pd
    return(phgd)

def graph_distro(phgd):
    """Graph the probability distribution produced by applying Bayes theorem.
    """
    x = []
    y = phgd
    for i in range(0, len(y)):
        x.extend([i]) 
    ax2 = plt.subplot(212) # creates second axis
    plt.bar(x,y)
    # could use plt.plot, but that would suggest a continuous distribution
    plt.grid()
    plt.xlabel('$H (outcome-type)$')
    plt.ylabel('$P(H|D)$')
    plt.title('probabilty distribution')
    plt.show()

def input_calc_updates(ph, pdgh):
    """ Input number of updates and calculate the phgd. 
    After getting the data (the numbers of actual successes and failures), 
    apply each of the 2 functions:
    failure_update(ph, pdgh)
    success_update(ph, pdgh)
    Between each update set ph = pdgh_t_ph.
    After all the updates, normalize the pdgh_t_h to phgd (saves time, 
    instead of normalizing after each update.   
    """
    num_succ_upd = eval(input('enter number of success updates '))
    num_fail_upd = eval(input('enter number of failure updates '))

    for i in range(0,num_succ_upd):
        pdgh_t_ph = success_update(ph, pdgh)
        ph = pdgh_t_ph
    for i in range(0,num_fail_upd):
        pdgh_t_ph = failure_update(ph, pdgh)
        ph = pdgh_t_ph
    phgd = calc_phgd(pdgh_t_ph)

    return phgd

def calc_products_in_numerator(ph, pdgh):
    """ Calculate the phgd_t_ph list using corresponding members of the pdgh 
    and ph lists. Same function as dice_loco_update()
    """
    num_h = len(ph)
    pdgh_t_ph = []
    for i in range (0, num_h):
        pdgh_t_ph.append(pdgh[i]*ph[i])
    #print("pdgh_t_ph ", pdgh_t_ph)
    return(pdgh_t_ph)




#if __name__ == '__main__':
#    main(*sys.argv)

