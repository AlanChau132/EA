from app import db, app
from app.models import User, Post, News, Picture, Comment


app_context = app.app_context()
app_context.push()
db.drop_all()
db.create_all()

u1 = User(username='john', email='john@example.com')
u2 = User(username='susan', email='susan@example.com')
u1.set_password("P@ssw0rd")
u2.set_password("P@ssw0rd")
db.session.add(u1)
db.session.add(u2)
u1.follow(u2)
u2.follow(u1)

p1 = Post(body='my first post!', author=u1)
p2 = Post(body='my first post!', author=u2)
db.session.add(p1)
db.session.add(p2)

# create some news
news1 = News(title='News 1', content='This is news 1')
news2 = News(title='News 2', content='This is news 2')
db.session.add(news1)
db.session.add(news2)
db.session.commit()  # Make sure to commit the changes so the news items get an ID

# create some pictures
picture1 = Picture(filename='picture1.jpg', description='This is picture 1', news_id=news1.id)
picture2 = Picture(filename='picture2.jpg', description='This is picture 2', news_id=news2.id)
db.session.add(picture1)
db.session.add(picture2)

# create some comments
comment1 = Comment(content='This is a comment for news 1', news_id=news1.id, author_id=u1.id)
comment2 = Comment(content='This is a comment for news 2', news_id=news2.id, author_id=u2.id)
db.session.add(comment1)
db.session.add(comment2)


# commit the changes
db.session.commit()

