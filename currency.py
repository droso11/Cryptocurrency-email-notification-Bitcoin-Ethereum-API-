import datetime

class Currency(object):
    def __init__(self, long_name, short_name, percent, min_update_time, function):
                # long_name - long name of currency.
                # percent - minimum of % to update
                # min_update_time = After this (in minutes) time if update doesn't occur, force update of (self.min, self.current, self.max, self.percent)
                # function to get the list of [min of 24h, current, max of 24h] currency price

        self.long_name = long_name
        self.short_name = short_name

        self.function = function
        self.min, self.last, self.max = self.function()
        self.current = self.last

        self.percent = 0.0
        self.min_percent = percent

        self._new_min = self.min
        self._new_max = self.max

        self.min_update_time = max(10, min_update_time)         # please do not update faster.
        self.last_update = datetime.datetime.now()

    def get_current_update_percent(self):
        self._new_min, self.current, self._new_max = self.function()
        self.percent = ((self.current - self.last) / self.last) * 100.0

    def __str__(self):
        return '{0}: {1:+.2f}%'.format(self.short_name, self.percent)

    def generate_title_body_list(self):
        title_list = []

        body_list = [
            '<b>{}</b>:'.format(str.upper(self.long_name)),

            'From <b>{}</b> to <b>{}</b>:'.format(
                str(self.last_update.replace(microsecond=0)), str(datetime.datetime.now().replace(microsecond=0))
            ),

            '{0} price: {1} PLN [{2:+.2f} %]'.format(self.long_name, self.current, self.percent)
        ]

        if abs(self.percent) >= self.min_percent:
            title_list.append(self.__str__())

        if self.min > self.current:
            title_list.append('{} hit lowest 24h'.format(self.short_name))
            body_list.append('{} hit the lowest value in 24h'.format(self.long_name))

        elif self.max < self.current:
            title_list.append('{} hit highest 24h'.format(self.short_name))
            body_list.append('{} hit the highest value in 24h'.format(self.long_name))

        return title_list, body_list

    def update(self):
        self.min = self._new_min
        self.max = self._new_max
        self.last = self.current
        self.last_update = datetime.datetime.now()

    def generate_mail_lists(self):
        self.get_current_update_percent()

        title, body = self.generate_title_body_list()

        if len(title):
            self.update()
        elif (datetime.datetime.now()-self.last_update).seconds//60 >= self.min_update_time:
            title.append(self.__str__())
            self.update()

        return title, body