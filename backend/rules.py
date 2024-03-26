from experta import *

class FeedingGuideline(Fact):
    pass

class FeedingExpert(KnowledgeEngine):

    @Rule(FeedingGuideline(age="6-8 months"))
    def feed_6_to_8_months(self):
        self.declare("6-8 months: Introduce thick porridge, mashed or pureed foods")
        self.declare("Frequency: 2-3 meals a day, frequent breastfeeding")
        self.declare("Amount: 2-3 tablespoons to half a 250 ml cup")

    @Rule(FeedingGuideline(age="9-11 months"))
    def feed_9_to_11_months(self):
        self.declare("9-11 months: Introduce finely chopped, diced or mashed foods")
        self.declare("Frequency: 3-4 meals a day, 1-2 snacks")
        self.declare("Amount: half to three quarters of a 250ml cup")

    @Rule(FeedingGuideline(age="12-23 months"))
    def feed_12_to_23_months(self):
        self.declare("12-23 months: Introduce chopped into small pieces or mashed if needed")
        self.declare("Frequency: 3-4 meals a day, 1-2 snacks")
        self.declare("Amount: three quarters to full 250ml cup")

    def get_recommendations(self, age_in_months):
        self.reset()
        if 6 <= age_in_months <= 8:
            self.declare(FeedingGuideline(age="6-8 months"))
        elif 9 <= age_in_months <= 11:
            self.declare(FeedingGuideline(age="9-11 months"))
        elif 12 <= age_in_months <= 23:
            self.declare(FeedingGuideline(age="12-23 months"))
        self.run()
        return '\n'.join(self.facts) 
