from app import db
from app.schemas import Review
from app.controllers.user_controller import UserController

UserController = UserController()

class ReviewModel(object):
    
    def __init__(self, reviews=[]):
        self.reviews = reviews


    def add_review(self, rev, bid, uid):    
        db.session.add(Review(rev["text"], bid, uid))
        db.session.commit()

    def get_business_reviews(self, bid):
        reviews = Review.query.filter_by(bid=bid).all()
        if not reviews:
            return {"success":False, "msg":"No Business Reviews"}
        output = []
        for r in reviews:
            r_obj = {
                'id':r.id,
                'text':r.text,
                'user':UserController.get_user(r.uid)["user"]
            }
            output.append(r_obj) 
        return {"success":True, "reviews":output}

