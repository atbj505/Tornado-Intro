class LiveText:
    def __init__(self, match_info, **kwargs):
        self.home_score = kwargs['home_score']
        self.visit_score = kwargs['visit_score']
        self.live_text = kwargs['live_text']

        self.period_cn = match_info['period_cn']
        self.home_team = match_info['home_team']
        self.visit_team = match_info['visit_team']

    def __repr__(self):
        return '%s %s %s : %s %s  %s' % (self.period_cn, self.home_team, self.home_score,
                                         self.visit_team, self.visit_score, self.live_text)
