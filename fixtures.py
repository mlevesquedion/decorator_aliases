from main import alias


@alias('average', 'avg')
def mean(lst):
    return sum(lst) / len(lst)
