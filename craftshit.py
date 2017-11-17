import json
import random

from flask import Flask, current_app
app = Flask(__name__)


def capitalize(s):
    """Make sure string starts with capital letter"""
    return s[0].capitalize() + s[1:] if len(s) > 0 else s


def beer_noun():
    """Generate a random noun for a beer"""

    nouns = ["US pale", "IPA", "stout", "ruby", "mild", "sour",
             "pale", "porter", "imperial stout", "small batch",
             "imperial pils"]
    return random.choice(nouns)


def desc_noun():
    """Generate a random noun to use to describe a beer"""

    nouns = ["peach", "red berry", "hops", "hell", "resin", "grapefruit",
             "tropical fruits", "chocolate", "lemongrass", "juniper",
             "lemon peel", "grains of paradise", "cloudberries", "mouthfeel"]

    modifiers = ["", "hints of", "notes of", "waves of", "a subtle hint of",
                 "a subtle note of", "a subtle wave of"]
    modifier = random.choice(modifiers)

    if modifier:
        return "{} {}".format(modifier, random.choice(nouns))
    else:
        return random.choice(nouns)


def beer_adj():
    """Generate a random adjective word or phrase"""

    adjs = ["black", "bitter", "light", "refreshing", "tart",
            "smokey", "roasted", "zesty", "tropical", "smoked",
            "intense", "rich", "golden", "intense", "powerful"]
    return random.choice(adjs)


def positive_adj():
    """Generic positive adjectives"""

    adjs = ["memorable", "legendary", "awesome", "magnificent",
            "cool", "majestic", "epic"]
    return random.choice(adjs)


def verb():
    """Generate a random verb"""
    verbs = ["overflowing", "bursting", "rounded out",
             "brimming", "nuanced", "packed"]
    return random.choice(verbs)


def adverb():
    """Generate a random adverb"""

    adverbs = ["totally", "truly", "friggin'"]
    return random.choice(adverbs)


def simile():
    """Generate a random simile to describe a beer"""
    return "{} as {}".format(beer_adj(), desc_noun())


def location():
    """Generate a brewing location"""
    
    locations = ["the mountains of Bavaria",
                 "the heart of Moscow's craft scene",
                 "New England",
                 "the Himalayan foothills",
                 "the forests of New England",
                 "Bohemia",
                 "the suburbs of Shoreditch"]
    return random.choice(locations)


def people():
    """Generate a brewer"""

    peeps = ["blind monks",
             "artisan craftsmen",
             "curators of fine ales",
             "brew masters",
             "bohemians",
             "men in white coats",
             "hip young interns",
             "himalayan hipsters",
             "Apple geniuses",
             "hops technicians"]
    return random.choice(peeps)


def time():
    """Generate a time in the past"""

    times = ["just last night",
             "a few seconds before we opened",
             "last Wednesday"]
    return random.choice(times)


def activity():
    """Hipster activities"""

    activities = ["writing your latest novel",
                  "worshipping an artisan burger",
                  "soaking up the latest from The Field",
                  "grooming one's epic beard",
                  "strolling {}".format(location()),
                  "riding around {} on your fixie bike".format(location()),
                  "purchasing your latest iPhone"]

    return random.choice(activities)
    

def beginning():
    """Generate a sentence for the start of the description"""
    
    beginnings = [
        "This {} is {} and {}."
        .format(beer_noun(), simile(), simile()),
        "Our {} is {} with {} and {}."
        .format(beer_noun(), verb(), desc_noun(), desc_noun()),
        "{}, {} and {}."
        .format(beer_adj(), beer_adj(), beer_adj()),
        "{}, {} and {} meet {} in this {}."
        .format(desc_noun(), desc_noun(), desc_noun(), desc_noun(),
                beer_noun())
    ]

    return random.choice(beginnings)


def middle(max_sentences):
    """Generate a sentence for the middle of the description"""

    middles = [
        ("Brewed in {} by {}, this {} is {} with {} and {}.")
        .format(location(), people(), beer_noun(), verb(), desc_noun(),
                desc_noun()),
        "Freshly imported from {} by {}.".format(location(), people()),
        "Unleashes {} combined with {}."
        .format(desc_noun(), desc_noun()),
        "Kegged {} by {} in {}.".format(time(), people(), location()),
        "The balance of {} and {} yield {} {} and {} with a {} finish."
        .format(desc_noun(), desc_noun(), desc_noun(), beer_adj(),
                desc_noun(), beer_adj())
    ]

    random.shuffle(middles)

    num_sentences = random.randint(0, max_sentences)
    return " ".join(capitalize(s) for s in middles[:num_sentences])
    
def ending():
    """Generate a sentence for the end of the description"""

    endings = [
        "Combine with {} whilst {} for a {} {} experience."
        .format(desc_noun(), activity(), adverb(), positive_adj()),
        "{} with {} and {}, {} and {}."
        .format(verb(), desc_noun(), desc_noun(), desc_noun(), desc_noun()),
        "{} and {}.".format(simile(), simile()),
        "Best enjoyed whilst {}.".format(activity()),
        "{} with {} and {}.".format(verb(), desc_noun(), desc_noun())
    ]

    return random.choice(endings)


def description():
    """Generate a random beer description"""
    sentences = []
    
    sentences.append(capitalize(beginning()))
    sentences.append(capitalize(middle(3)))
    sentences.append(capitalize(ending()))
    
    return " ".join(sentences)
    

def name():
    """Generate the beer name"""
    return ""
    

@app.route('/')
def index():
    """Main app entry point"""
    return current_app.send_static_file("index.html")

@app.route("/beer/")
def beer():
    """REST interface to get a random beer"""
    wrapper = "update({})"
    return wrapper.format(
        json.dumps({'name': name(), 'desc': description()}))
    

if __name__ == "__main__":

    print(description())
