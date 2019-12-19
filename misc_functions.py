
class Fibonacci:

    def fibo(self, num):
        if num <= 1:
            return num
        else:
            return self.fibo(num - 1) + self.fibo(num - 2)


class ConvertNumbertoString:

    def num2words(self, num):
        under_20 = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',
                    'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
        above_100 = {100: 'hundred', 1000: 'thousand', 1000000: 'million', 1000000000: 'billion'}

        if num < 20:
            return under_20[num]

        if num < 100:
            return tens[int(num / 10) - 2] + ('' if num % 10 == 0 else ' ' + under_20[num % 10])

        # find the appropriate pivot - 'Million' in 3,603,550, or 'Thousand' in 603,550
        pivot = max([key for key in above_100.keys() if key <= num])

        return self.num2words(int(num / pivot)) + ' ' + above_100[pivot] + (
            '' if num % pivot == 0 else ' ' + self.num2words(num % pivot))
