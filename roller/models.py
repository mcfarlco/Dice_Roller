from datetime import *
from roller import db


class Roll_History(db.Model):
    roll_id = db.Column(db.Integer, primary_key=True)
    d2 = db.Column(db.Integer, default=0)
    d2_result = db.relationship("D2_Results", backref="d2_results", lazy=True)
    d3 = db.Column(db.Integer, default=0)
    d3_result = db.relationship("D3_Results", backref="d3_results", lazy=True)
    d4 = db.Column(db.Integer, default=0)
    d4_result = db.relationship("D4_Results", backref="d4_results", lazy=True)
    d6 = db.Column(db.Integer, default=0)
    d6_result = db.relationship("D6_Results", backref="d6_results", lazy=True)
    d8 = db.Column(db.Integer, default=0)
    d8_result = db.relationship("D8_Results", backref="d8_results", lazy=True)
    d10 = db.Column(db.Integer, default=0)
    d10_result = db.relationship("D10_Results", backref="d10_results", lazy=True)
    d12 = db.Column(db.Integer, default=0)
    d12_result = db.relationship("D12_Results", backref="d12_results", lazy=True)
    d20 = db.Column(db.Integer, default=0)
    d20_result = db.relationship("D20_Results", backref="d20_results", lazy=True)
    d100 = db.Column(db.Integer, default=0)
    d100_result = db.relationship("D100_Results", backref="d100_results", lazy=True)

    def __repr__(self):
        return f"Roll_History('{self.id}', '{self.d2}', '{self.d3}', '{self.d4}', '{self.d6}', '{self.d8}', '{self.d10}', '{self.d12}', '{self.d20}', '{self.d100}')"


class D2_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D2_Results('{self.result}')"


class D3_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D3_Results('{self.result}')"


class D4_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D4_Results('{self.result}')"


class D6_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D6_Results('{self.result}')"


class D8_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D8_Results('{self.result}')"


class D10_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D10_Results('{self.result}')"


class D12_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D12_Results('{self.result}')"


class D20_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D20_Results('{self.result}')"


class D100_Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey(
        "roll_history.roll_id"), nullable=False)

    def __repr__(self):
        return f"D100_Results('{self.result}')"






# db.create_all()
# user_1 = User(username="Testname", email="test@gmail.com", password="password")
# user_2 = User(username="Testname2", email="test@gmail.com2", password="password")
# db.session.add(user_1)
# db.session.add(user_2)
# db.sessoin.commit()
# User.query.all()
# User.query.filter_by(username="EXACT").all()
# User.query.get(ID#)
# user = User.query.filter_by(username="Testname").all()
# user.id # prints 1
# post_1 = Post(title="Title 1", content="Content One", user_id=user.id)
# db.session.add(post_1)
# db.session.commit()
# post = Post.query.first()
# post.user_id # prints 1
# post.author # prints User query
# db.drop_all()
