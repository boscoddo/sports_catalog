import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Categories, Items, Users


engine = create_engine('sqlite:///sportscatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

# Create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Creating Dummy User
User1 = Users(name="jon doe", email="jondoe@yahoo.com")
session.add(User1)
session.commit()

# Creating generic sports categories
category = Categories(name='Soccer', user_id=1)
session.add(category)
session.commit()
soccer = session.query(Categories).filter_by(name='Soccer').one()

category = Categories(name='Basketball', user_id=1)
session.add(category)
session.commit()
basketball = session.query(Categories).filter_by(name='Basketball').one()

category = Categories(name='Baseball', user_id=1)
session.add(category)
session.commit()
baseball = session.query(Categories).filter_by(name='Baseball').one()

category = Categories(name='Frisbee', user_id=1)
session.add(category)
session.commit()
frisbee = session.query(Categories).filter_by(name='Frisbee').one()

category = Categories(name='Snowboarding', user_id=1)
session.add(category)
session.commit()
snowboarding = session.query(Categories).filter_by(name='Snowboarding').one()

category = Categories(name='Rock Climbing', user_id=1)
session.add(category)
session.commit()
rock_climbing = session.query(Categories).filter_by(name='Rock Climbing').one()

category = Categories(name='Foosball', user_id=1)
session.add(category)
session.commit()
foosball = session.query(Categories).filter_by(name='Foosball').one()

category = Categories(name='Skating', user_id=1)
session.add(category)
session.commit()
skating = session.query(Categories).filter_by(name='Skating').one()

category = Categories(name='Hockey', user_id=1)
session.add(category)
session.commit()
hockey = session.query(Categories).filter_by(name='Hockey').one()


item = Items(name='Wilson Traditional Soccer Ball',
             photo=('/static/img/soccer.jpg'),
             description=('The traditional soccer balls have an updated'
                        ' tradional look. Shiney material cover and 32'
                        ' panel machine sewn construction.'),
             category=soccer,
             price="$46.99",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Spalding NBA Street Basketball',
             photo=('/static/img/basketball.jpg'),
             description=('Official nba size and weight. Designed to'
                        ' withstand the competitive street game.'
                        ' Durable rubber outdoor cover with deep'
                        ' channels for incredible grip.'),
             category=basketball,
             price="$17.99",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Rawlings Official League Baseballs,',
             photo=('/static/img/baseball.jpg'),
             description=('"The Rawlings OLB3 Recreational Use Baseballs'
                        ' are designed with a solid cork and rubber center'
                        ' with a synthetic leather cover to create an easy'
                        ' grip in addition to major league seams. These 24'
                        ' baseballs come in a convenient, durable white'
                        ' bucket sporting the MLB logo and the iconic'
                        ' Rawlings patch. They are suitable for recreational'
                        ' use of ages 8 and under. They are official size'
                        ' and weight and are the #1 choice of leagues,'
                        ' coaches, parents, and players in North America."'),
             category=baseball,
             price="$57.68",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Discraft 175 gram Ultra Star Sport Disc',
             photo=('/static/img/frisbee.jpg'),
             description=('The world standard for the sport of Ultimate,'
                        ' and official disc of the USA Ultimate'
                        ' Championship Series since 1991. With its'
                        ' contoured grip and aerodynamic engineering,'
                        ' the Ultra-Star has set the standard for quality,'
                        ' consistency, and performance.'),
             category=frisbee,
             price="$9.05",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='STAUBER Summit Snowboard',
             photo=('/static/img/snowboarding.jpg'),
             description=('The Stauber Summit Snowboard is a high quality'
                        ' snowboard. Its innovative technology allows for'
                        ' a comfortable all mountain style of riding, in'
                        ' addition to an exhilarating park experience.'
                        ' The board shape prevents riders from catching'
                        ' an edge in snowy or icy conditions. With its'
                        ' twin directional shape and its camber rocker'
                        ' camber profile, the STAUBER Summit is perfect'
                        ' for a fun day on the mountain. Its designed to'
                        ' accommodate all levels of riding. From beginner'
                        ' to expert level, any rider will enjoy this'
                        ' snowboards unique handling qualities.'),
             category=snowboarding,
             price="$149.83",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Black Diamond Momentum Harness',
             photo=('/static/img/rockclimbing.jpg'),
             description=('For all-around climbers who know that time'
                        ' spent fiddling with leg loops and adjusting'
                        ' a pinching waistbelt is time wasted, the Black'
                        ' Diamond Momentum delivers a time-saving design'
                        ' for all styles of climbing.'),
             category=rock_climbing,
             price="$109.86",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Warrior Professional Foosball Table',
             photo=('/static/img/foosball.jpg'),
             description=('Warrior the official table of the Professional'
                        ' Foosball Tour is a top caliber, durable, player'
                        ' friendly table that is made for the professional'
                        ' player and available to the general public and'
                        ' perfect for youth programs.'),
             category=foosball,
             price="$599.99",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='American Athletic Skates',
             photo=('/static/img/skating.jpg'),
             description=('Best selling entry level skates. The'
                        ' tricot lined skates are comfortable, fits'
                        ' well and has an easy care durable PVC boot. The'
                        ' skates features multi layered ankle support,'
                        ' hollow ground, nickel plated steel blade, full'
                        ' quarter padding for comfort and a form fitting'
                        ' padded tongue.'),
             category=skating,
             price="$55.92",
             user_id=1)
session.add(item)
session.commit()

item = Items(name='Franklin Sports Hockey Stick',
             photo=('/static/img/hockey.jpg'),
             description=('Our Franklin Sports NHL SX Comp 1010 Street'
                        ' Tech Hockey Stick has a multi-ply poplar/birch'
                        ' shaft and replaceable high-impact polymer blade.'
                        ' 52" in length, designed for junior play. Assorted'
                        ' colors.'),
             category=hockey,
             price="$19.99",
             user_id=1)
session.add(item)
session.commit()

print('Database Populated')