from msgint.segment import textseg

class BaseClassifier:
    def __init__(self):
        self.features = {}
        self.categories = {}
        
    def inc_feature(self, feature, cat):
        self.features.setdefault(feature, {})
        self.features[feature].setdefault(cat, 0)
        self.features[feature][cat] += 1
        
    def inc_category(self, cat):
        self.categories.setdefault(cat, 0)
        self.categories[cat] += 1
        
    def feature_count(self, feature, cat):
        if feature in self.features and cat in self.features[cat]:
            return float(self.features[feature][cat])
        return 0.0
    
    def category_count(self, cat):
        if cat in self.categories:
            return float(self.categories[cat])
        return
    
    def category_total(self):
        return sum(self.categories.values())
    
    def get_categories(self):
        return self.categories.keys()
    
    def get_feature(self, sample):
        return textseg.feature_smallseg(sample)
    
    def train(self, sample, cat):
        fs = self.get_feature(sample)
        for f in fs:
            self.inc_feature(f, cat)
        self.inc_category(cat)
        
    def feature_prob(self, feature, cat):
        if self.category_count(cat) == 0:
            return 0
        return self.feature_count(feature, cat) / self.category_count(cat)
    
    def weighted_prob(self, feature, cat, weight = 1, ap = 0.5):
        p = self.feature_prob(feature, cat)
        t = sum([self.feature_count(feature, c) for c in self.get_categories()])
        return ((weight * ap) + (t * p)) / (weight + t)