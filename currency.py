import datetime

class Currency(object):
    def __init__(self, long_name, short_name, currency_short, percent, min_update_time, function):
                # long_name - long name of CRYPTOcurrency.
                # short_name - CRYPTOcurrency
                # currency_short - CURRENCY (USD/PLN etc)
                # percent - minimum of % change in value to update
                # min_update_time = After this (in minutes) time if update doesn't occur \
                # \force update of (self.min, self.current, self.max, self.percent)
                # function to get the list of [min of 24h, current, max of 24h] currency price

        self.long_name = long_name
        self.short_name = short_name

        self.function = function
        self.min, self.last, self.max = self.function()
        self.current = self.last

        self.percent = 0.0
        self.min_percent = percent

        self._min = self.min
        self._max = self.max

        self.min_update_time = max(10, min_update_time)         # please do not update faster.
        self.last_update = datetime.datetime.now()
        self.currency_short = currency_short

    def get_current_update_percent(self):
        self._min, self.current, self._max = self.function()
        self.percent = self.get_percent(self.last, self.current)



    def __str__(self):
        return '{0}: {1}{2} ({3:+.2f}%)'.format(self.short_name, self.current, self.currency_short, self.percent)

    def get_percent(self, old, new):
        return ((new-old)/old) * 100.0

    def generate_title_body_list(self):
        title_list = []

        body_list = [
            '<b>{}</b>:'.format(str.upper(self.long_name)),

            'From <b>{}</b> to <b>{}</b>:'.format(
                str(self.last_update.replace(microsecond=0)), str(datetime.datetime.now().replace(microsecond=0))
            ),

            '{0} price: {1} {2} [{3:+.2f} %]'.format(
                self.long_name, self.current, self.currency_short, self.percent
            )
        ]

        if abs(self.percent) >= self.min_percent:
            title_list.append(self.__str__())

        if self.get_percent(self.last, self.current) >= 1:
            if self.min > self.current:
                title_list.append('{} hit lowest 24h'.format(self.short_name))
                body_list.append('{} hit the lowest value in 24h'.format(self.long_name))

            elif self.max < self.current:
                title_list.append('{} hit highest 24h'.format(self.short_name))
                body_list.append('{} hit the highest value in 24h'.format(self.long_name))

        return title_list, body_list

    def update(self):
        self.min, self._min = self._min, self.min
        self.max, self._max = self._max, self.max
        self.last = self.current
        self.last_update = datetime.datetime.now()

    def generate_mail_lists(self):
        self.get_current_update_percent()

        title, body = self.generate_title_body_list()

        if len(title):
            self.update()

        elif self.min_update_time > 0 \
            and (datetime.datetime.now()-self.last_update).seconds//60 >= self.min_update_time \
            and self.get_percent(self.last, self.current) >= 1:

            title.append(self.__str__())
            self.update()

        return title, body