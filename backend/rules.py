from experta import *

class FeedingGuideline(Fact):
    pass

class FeedingExpert(KnowledgeEngine):

    @Rule(FeedingGuideline(age="6-8 months"))
    def feed_6_to_8_months(self):
        print("6-8 months: Introduce thick porridge, mashed or pureed foods")
        print("Frequency: 2-3 meals a day, frequent breastfeeding")
        print("Amount: 2-3 tablespoons to half a 250 ml cup")

    @Rule(FeedingGuideline(age="9-11 months"))
    def feed_9_to_11_months(self):
        print("9-11 months: Introduce finely chopped, diced or mashed foods")
        print("Frequency: 3-4 meals a day, 1-2 snacks")
        print("Amount: half to three quarters of a 250ml cup")

    @Rule(FeedingGuideline(age="12-23 months"))
    def feed_12_to_23_months(self):
        print("12-23 months: Introduce chopped into small pieces or mashed if needed")
        print("Frequency: 3-4 meals a day, 1-2 snacks")
        print("Amount: three quarters to full 250ml cup")

engine = FeedingExpert()
engine.reset()
engine.declare(FeedingGuideline(age="6-8 months"))
engine.run()
