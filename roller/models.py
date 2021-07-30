from datetime import *
from roller import db


class Rollhistory(db.Model):
    roll_id = db.Column(db.Integer, primary_key=True)
    n_die = db.Column(db.Integer, default=0)
    sum_die = db.Column(db.Integer, default=0)
    d2 = db.Column(db.Integer, default=0)
    d2_result = db.relationship('D2_Results', back_populates='d2_result', lazy=True)
    d3 = db.Column(db.Integer, default=0)
    d3_result = db.relationship("D3_Results", back_populates="d3_result", lazy=True)
    d4 = db.Column(db.Integer, default=0)
    d4_result = db.relationship("D4_Results", back_populates="d4_result", lazy=True)
    d6 = db.Column(db.Integer, default=0)
    d6_result = db.relationship("D6_Results", back_populates="d6_result", lazy=True)
    d8 = db.Column(db.Integer, default=0)
    d8_result = db.relationship("D8_Results", back_populates="d8_result", lazy=True)
    d10 = db.Column(db.Integer, default=0)
    d10_result = db.relationship("D10_Results", back_populates="d10_result", lazy=True)
    d12 = db.Column(db.Integer, default=0)
    d12_result = db.relationship("D12_Results", back_populates="d12_result", lazy=True)
    d20 = db.Column(db.Integer, default=0)
    d20_result = db.relationship("D20_Results", back_populates="d20_result", lazy=True)
    d100 = db.Column(db.Integer, default=0)
    d100_result = db.relationship("D100_Results", back_populates="d100_result", lazy=True)

    def __repr__(self):
        return f"Rollhistory('{self.roll_id}', \
                                '{self.d2}', \
                                '{self.d2_result}', \
                                '{self.d3}', \
                                '{self.d3_result}', \
                                '{self.d4}', \
                                '{self.d4_result}', \
                                '{self.d6}', \
                                '{self.d6_result}', \
                                '{self.d8}', \
                                '{self.d8_result}', \
                                '{self.d10}', \
                                '{self.d10_result}', \
                                '{self.d12}', \
                                '{self.d12_result}', \
                                '{self.d20}', \
                                '{self.d20_result}', \
                                '{self.d100}, \
                                '{self.d100_result}')"


class D2_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey('rollhistory.roll_id'), nullable=False)
    d2_result = db.relationship("Rollhistory", back_populates="d2_result")

    def __repr__(self):
        return f"D2_Results('{self.result}')"


class D3_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d3_result = db.relationship("Rollhistory", back_populates="d3_result")

    def __repr__(self):
        return f"D3_Results('{self.result}')"


class D4_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d4_result = db.relationship("Rollhistory", back_populates="d4_result")

    def __repr__(self):
        return f"D4_Results('{self.result}')"


class D6_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d6_result = db.relationship("Rollhistory", back_populates="d6_result")

    def __repr__(self):
        return f"D6_Results('{self.result}')"


class D8_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d8_result = db.relationship("Rollhistory", back_populates="d8_result")

    def __repr__(self):
        return f"D8_Results('{self.result}')"


class D10_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d10_result = db.relationship("Rollhistory", back_populates="d10_result")

    def __repr__(self):
        return f"D10_Results('{self.result}')"


class D12_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d12_result = db.relationship("Rollhistory", back_populates="d12_result")

    def __repr__(self):
        return f"D12_Results('{self.result}')"


class D20_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d20_result = db.relationship("Rollhistory", back_populates="d20_result")

    def __repr__(self):
        return f"D20_Results('{self.result}')"


class D100_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    roll_id = db.Column(db.Integer, db.ForeignKey("rollhistory.roll_id"), nullable=False)
    d100_result = db.relationship("Rollhistory", back_populates="d100_result")

    def __repr__(self):
        return f"D100_Results('{self.result}')"


class Modifiers(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    advantage = db.Column(db.Boolean, default=0)
    disadvantage = db.Column(db.Boolean, default=0)
    explode = db.Column(db.Boolean, default=0)
    cheater = db.Column(db.Boolean, default=0)

    def __repr__(self):
        return f"Modifiers('{self.advantage}', '{self.disadvantage}', '{self.explode}', '{self.cheater}')"
