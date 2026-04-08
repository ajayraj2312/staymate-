# ============================================================
#  Rental Preference AI - LLM Fine-Tuning Dataset
#  Format : OpenAI / Anthropic chat fine-tuning style
#  Each entry: { "messages": [ {role, content}, ... ] }
#  100+ diverse conversation samples
# ============================================================

dataset = [

    # ── SAMPLE 1 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 24-year-old student looking for a cheap place near my university."},
            {"role": "assistant", "content": "Great! For a student on a budget, I'd recommend a furnished studio or a room in a shared house near the university. These are usually the most affordable options and keep your commute short. What's your monthly budget?"}
        ]
    },

    # ── SAMPLE 2 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 35, married with two kids. We need at least 3 bedrooms and a yard."},
            {"role": "assistant", "content": "A family of four with two children would be very comfortable in a house or townhouse with 3+ bedrooms. A yard is a great call for kids. I'd suggest looking in quiet suburban neighborhoods which tend to offer more space at a reasonable price. Do you have a city or area in mind?"}
        ]
    },

    # ── SAMPLE 3 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I work fully remote and I'm single. I just want something cozy and affordable in a nice neighborhood."},
            {"role": "assistant", "content": "Since you work remotely, you have great flexibility on location! A furnished studio or 1-bedroom apartment in a quiet neighborhood would be ideal. You'll want reliable internet as a top priority. Would you prefer a city-center vibe or something more suburban and peaceful?"}
        ]
    },

    # ── SAMPLE 4 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I have a dog. A lot of places don't allow pets. What should I look for?"},
            {"role": "assistant", "content": "Pet-friendly rentals are definitely the key filter for you! Look specifically for listings that mention 'pets allowed' or 'pet-friendly.' Houses and ground-floor apartments tend to be more accommodating. A property near a park would also be a big plus for your dog's daily walks. Would you like tips on negotiating pet deposits?"}
        ]
    },

    # ── SAMPLE 5 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "My budget is $800 a month. Is that realistic for a 1-bedroom in a big city?"},
            {"role": "assistant", "content": "It depends on the city! $800/month for a 1-bedroom is very doable in smaller cities like Columbus, Indianapolis, or Memphis. In places like New York, San Francisco, or Los Angeles, $800 would more realistically get you a room in a shared apartment. Would you like suggestions for affordable cities that fit your budget?"}
        ]
    },

    # ── SAMPLE 6 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 29, a software engineer. I want modern amenities — gym, parking, rooftop if possible."},
            {"role": "assistant", "content": "You're describing a luxury apartment building or a high-end condo! These typically come with amenities like a fitness center, covered parking, and sometimes rooftop access. They tend to be in the $1,800–$3,500 range depending on the city. Would you prefer a city-center location to be close to tech hubs, or are you open to a transit-connected suburb?"}
        ]
    },

    # ── SAMPLE 7 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What's the difference between a furnished and unfurnished apartment?"},
            {"role": "assistant", "content": "A furnished apartment comes with essential furniture like a bed, sofa, dining table, and sometimes kitchen appliances. It's great if you're moving quickly or don't own furniture yet. An unfurnished apartment is an empty space — you bring everything, but rent is typically lower and you can personalize the space completely. Semi-furnished falls in between, usually including large appliances but not furniture."}
        ]
    },

    # ── SAMPLE 8 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 62 and recently widowed. I want something small, safe, and easy to maintain."},
            {"role": "assistant", "content": "I'm sorry for your loss. A ground-floor condo or a small 1-bedroom apartment in a safe, well-maintained community would suit you well. Look for buildings with a property manager on-site, security features, and ideally close to medical facilities or public transit. Would you like help identifying what safety features to prioritize?"}
        ]
    },

    # ── SAMPLE 9 ─────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm moving to a new city for work and only need a place for 6 months."},
            {"role": "assistant", "content": "For a short-term stay, I'd recommend looking for month-to-month leases or furnished apartments that offer flexible 6-month lease terms. Serviced apartments and corporate housing are also worth exploring — they're designed for exactly this scenario and typically include utilities and internet in the price. What city are you moving to?"}
        ]
    },

    # ── SAMPLE 10 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "Can you explain what a lease term means and which is best for me as a first-time renter?"},
            {"role": "assistant", "content": "A lease term is the agreed duration you commit to renting a property. Common options are: Month-to-Month (maximum flexibility, slightly higher rent), 6-Month (good trial period), and 1-Year (most common, usually the best value). As a first-time renter, a 1-year lease is a solid starting point — it gives you stability and is generally the easiest to get approved for. If you're unsure about the location, a 6-month lease offers a nice balance."}
        ]
    },

    # ── SAMPLE 11 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 45, a nurse working night shifts. I need a quiet place where I can sleep during the day."},
            {"role": "assistant", "content": "A quiet environment is absolutely critical for shift workers. I'd suggest a ground-floor or top-floor unit in a low-traffic building to minimize hallway and neighbor noise. Suburban or residential neighborhoods tend to be much quieter than city centers during the day. Also look for units with double-pane windows. Would you like tips on what questions to ask a landlord about noise?"}
        ]
    },

    # ── SAMPLE 12 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I have a family of 5 with a $2000/month budget. Any advice?"},
            {"role": "assistant", "content": "A $2,000/month budget for a family of 5 will go much further in mid-size cities than in major metros. Look for 3-bedroom houses or townhouses in suburban areas. Cities like Columbus, Indianapolis, San Antonio, or Charlotte often have spacious rentals in that range. You may also find duplexes with yards that offer great value. Do you have a preferred region of the country?"}
        ]
    },

    # ── SAMPLE 13 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 21, non-binary, and moving out for the first time. I'm nervous about the process."},
            {"role": "assistant", "content": "Moving out for the first time is exciting and it's totally normal to feel nervous! Here's a quick checklist: 1) Set a budget (rent should ideally be under 30% of income), 2) Gather documents (ID, income proof, references), 3) Visit multiple places before deciding, 4) Read the lease carefully before signing, 5) Budget for a security deposit (usually 1–2 months rent). Would you like help figuring out what type of place fits your lifestyle?"}
        ]
    },

    # ── SAMPLE 14 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I earn $45,000 a year. What rent range is realistic for me?"},
            {"role": "assistant", "content": "The general rule is to spend no more than 30% of your gross monthly income on rent. At $45,000/year, that's about $3,750/month gross or roughly $1,125/month on rent. If you're in a high cost-of-living city, you may need a roommate or look at a studio to stay within budget. In a mid-size city, a comfortable 1-bedroom should be achievable. Would you like suggestions based on your target city?"}
        ]
    },

    # ── SAMPLE 15 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What amenities should a young professional prioritize?"},
            {"role": "assistant", "content": "For a young professional, the most valuable amenities are usually: fast and reliable internet, in-unit or on-site laundry, secure parking or easy transit access, a gym to skip the gym membership, and a workspace or co-working area. Location matters a lot too — being close to restaurants, coffee shops, and nightlife can greatly improve quality of life. What's your biggest day-to-day priority?"}
        ]
    },

    # ── SAMPLE 16 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want to live near public transport. What property type is best?"},
            {"role": "assistant", "content": "Apartments and condos near transit hubs are your best bet. Urban areas along metro, subway, or bus lines tend to have dense apartment buildings within walking distance of stops. Studios and 1-bedrooms are most common in these locations. If you don't own a car, being near a transit hub is a smart financial decision — it can save you hundreds per month. Any specific city you're looking at?"}
        ]
    },

    # ── SAMPLE 17 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "How many occupants can legally live in a 1-bedroom apartment?"},
            {"role": "assistant", "content": "The general standard in the US is 2 people per bedroom plus 1 additional occupant. So for a 1-bedroom, up to 3 people is typically considered acceptable. However, local housing codes and individual landlord policies vary. Some landlords apply stricter rules. If you're planning to live with a partner or a child, always disclose this upfront to avoid lease violations."}
        ]
    },

    # ── SAMPLE 18 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 50 and retired. I want somewhere warm, affordable, and peaceful."},
            {"role": "assistant", "content": "Retirement is a great time to optimize for quality of life! For warm, affordable, and peaceful living, cities like San Antonio TX, Tucson AZ, Las Vegas NV, or Jacksonville FL often come up as top picks. A 1-bedroom condo or a small house in a 55+ community or a quiet suburb would be ideal. Do you prefer a more urban feel or a truly relaxed, nature-oriented setting?"}
        ]
    },

    # ── SAMPLE 19 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm looking for a place with a pool. Which property types typically have pools?"},
            {"role": "assistant", "content": "Pools are most commonly found in apartment complexes and condo buildings, especially in warmer states like Florida, Texas, Arizona, and California. Luxury apartment buildings in most cities often include a rooftop or ground-level pool. Some upscale townhouse communities also have shared pools. Private pools in rental houses exist but are less common and usually come with a higher price tag."}
        ]
    },

    # ── SAMPLE 20 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What is a security deposit and how much should I expect to pay?"},
            {"role": "assistant", "content": "A security deposit is a refundable amount you pay upfront to cover potential damages or unpaid rent. Most landlords charge 1–2 months' rent as a deposit. Some states cap it by law — for example, California limits it to 2 months for unfurnished and 3 months for furnished units. You should get it back within 14–30 days after moving out, minus any legitimate deductions for damages beyond normal wear and tear."}
        ]
    },

    # ── SAMPLE 21 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 30, female, and moving solo to a new city. Safety is my top concern."},
            {"role": "assistant", "content": "Safety is an excellent priority. Here are key things to check: 1) Research neighborhood crime statistics on sites like NeighborhoodScout or local police portals, 2) Look for buildings with controlled entry, cameras, and on-site management, 3) Visit the area at different times of day, 4) Ask current residents about their experience, 5) Ensure door locks and window latches are in good condition. Would you like a checklist of safety questions to ask a landlord?"}
        ]
    },

    # ── SAMPLE 22 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a freelancer with irregular income. Will landlords rent to me?"},
            {"role": "assistant", "content": "Freelancers can absolutely rent — you just need to document your income differently. Landlords typically want proof of income 2–3x the monthly rent. For freelancers, you can provide: bank statements (3–6 months), tax returns, client contracts, or PayPal/invoice records. Some landlords may ask for a larger deposit or a co-signer. Private landlords are often more flexible than large property management companies."}
        ]
    },

    # ── SAMPLE 23 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What is the best property type for a couple with no kids?"},
            {"role": "assistant", "content": "For a couple without kids, a 1-bedroom or 2-bedroom apartment, condo, or townhouse works very well. A second bedroom doubles as a home office or guest room. Condos are especially popular with couples for their balance of space, amenities, and lower maintenance versus a house. If you both work from home, a 2-bedroom with good natural light and quiet surroundings is well worth the extra cost."}
        ]
    },

    # ── SAMPLE 24 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I have a PhD and earn above $150K. What kind of rental options are available for me?"},
            {"role": "assistant", "content": "With a high income, you have access to the full spectrum of rental options. You could consider: luxury condos or penthouses in city centers, spacious houses in premium suburban neighborhoods, or furnished executive apartments. High-end buildings with concierge service, smart home features, and premium amenities are well within your range. Would you prioritize urban lifestyle or space and privacy?"}
        ]
    },

    # ── SAMPLE 25 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want to rent near a good school district. Any tips?"},
            {"role": "assistant", "content": "School district quality is a great consideration even if you're renting. Websites like GreatSchools.org and Niche.com rate school districts and let you filter by area. Suburban neighborhoods in cities like Boston, San Jose, and Denver often have top-rated public schools. Keep in mind that rentals near good school districts tend to be priced higher due to demand. Houses and townhouses in these areas are the most common rental type for families."}
        ]
    },

    # ── SAMPLE 26 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I prefer month-to-month leases. Are there downsides to this?"},
            {"role": "assistant", "content": "Month-to-month leases offer maximum flexibility, which is great if you're unsure about your plans. The main downsides are: 1) Higher monthly rent (usually 10–20% more than a 1-year lease), 2) Less security — landlords can end the tenancy with 30–60 days notice, 3) Fewer landlords offer it. It's ideal for people between jobs, exploring a new city, or waiting to buy a home. If you value flexibility over savings, it's a solid choice."}
        ]
    },

    # ── SAMPLE 27 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 40, a teacher with two cats. What should I know before renting?"},
            {"role": "assistant", "content": "As a teacher with cats, here's what to look for: 1) Filter specifically for pet-friendly listings that allow cats, 2) Expect a pet deposit of $200–$500 per cat, or a monthly pet fee of $25–$75, 3) Look for buildings with no-carpet flooring options which are easier to clean, 4) Ground-floor or buildings with a small outdoor area are great for cats. Some landlords are more flexible with cats vs dogs since cats are typically quieter. Always disclose your pets upfront."}
        ]
    },

    # ── SAMPLE 28 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "Is it cheaper to rent a room in a shared house than a studio?"},
            {"role": "assistant", "content": "Yes, in most cities a room in a shared house is significantly cheaper than a studio. Renting a room typically costs 30–50% less because you share the total rent and utilities. However, you'll share common areas like the kitchen and bathroom. A studio gives you full privacy, your own kitchen, and no housemate dynamics to manage. For someone on a tight budget who is sociable, a shared house is excellent value. For those valuing privacy, a studio is worth the extra cost."}
        ]
    },

    # ── SAMPLE 29 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What questions should I ask when touring an apartment?"},
            {"role": "assistant", "content": "Great question! Here are the most important things to ask: 1) What utilities are included in rent? 2) What's the pet policy? 3) How is maintenance handled and what's the response time? 4) Is there parking included or available? 5) What are the noise levels like? 6) What is the lease break policy? 7) Has there been any history of pest issues? 8) How secure is the building? 9) Is subletting allowed? 10) Are there plans to raise rent at renewal? Would you like these in a printable checklist format?"}
        ]
    },

    # ── SAMPLE 30 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 27, male, just got my first job earning $55K. What property type and budget should I aim for?"},
            {"role": "assistant", "content": "Congrats on the new job! At $55K/year, your ideal rent budget is around $1,100–$1,375/month (25–30% of gross income). A furnished studio or a 1-bedroom apartment in a mid-tier neighborhood would be a great starting point. Consider a place with laundry in-unit and good transit access to cut other costs. If you're in a higher cost-of-living city, a room in a shared apartment is a smart move for the first year while you build savings."}
        ]
    },

    # ── SAMPLE 31 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 33 and going through a divorce. I need a place quickly and don't want anything long-term."},
            {"role": "assistant", "content": "I'm sorry you're going through that. For a quick, short-term solution, look for: furnished apartments with month-to-month or 3–6 month leases, extended stay hotels or serviced apartments (which include utilities and internet), or rooms in shared houses that are immediately available. Many platforms like Furnished Finder, Airbnb long-stay, or Facebook Marketplace have flexible listings. Would you like advice on what documents to have ready to speed up the application?"}
        ]
    },

    # ── SAMPLE 32 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What does semi-furnished mean exactly?"},
            {"role": "assistant", "content": "Semi-furnished typically means the unit includes major appliances and built-in fixtures but not furniture. You can usually expect: a refrigerator, stove/oven, dishwasher, and sometimes a washer/dryer. What you won't find is a sofa, bed frame, mattress, or dining table — you need to bring those yourself. It's a good middle ground: cheaper than fully furnished, but you don't need to buy appliances. Perfect if you have some furniture but don't want to haul heavy appliances."}
        ]
    },

    # ── SAMPLE 33 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I prefer to live close to nature and parks. What should I look for?"},
            {"role": "assistant", "content": "Nature lovers should target: neighborhoods adjacent to city parks, greenbelts, or waterfronts; properties in suburbs near trails or nature reserves; and cities known for outdoor access like Denver, Portland, Seattle, or Austin. Ground-floor apartments or houses with private outdoor space are a bonus. Use Google Maps to check proximity to parks when browsing listings. Would you like a list of US cities ranked by green space and outdoor access?"}
        ]
    },

    # ── SAMPLE 34 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 55, recently retired, and my income is fixed. How do I make sure rent stays affordable long-term?"},
            {"role": "assistant", "content": "Great thinking ahead! Here are strategies for long-term affordability: 1) Look for rent-stabilized or rent-controlled apartments in cities that have such laws, 2) Sign longer leases (2-year) to lock in current rates, 3) Consider 55+ communities which often offer competitive pricing, 4) Look into HUD housing assistance programs if income is below certain thresholds, 5) Smaller cities and suburbs offer more stable and affordable rents. Would you like information on any of these options in detail?"}
        ]
    },

    # ── SAMPLE 35 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "How does renting a condo differ from renting an apartment?"},
            {"role": "assistant", "content": "The main differences are ownership and management structure. An apartment is owned by a single landlord or company that manages all units. A condo is individually owned — you're renting from the private owner. Condos often feel more personalized and may have higher-end finishes. However, you're subject to both the owner's rules and the condo association's rules (HOA). Apartments usually offer more standardized lease processes. Both can be excellent choices — condos often feel more like a home."}
        ]
    },

    # ── SAMPLE 36 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 19-year-old looking for my first apartment with $500/month budget."},
            {"role": "assistant", "content": "At $500/month, your best options are: renting a room in a shared house (very common for this budget), student housing near a university, or looking in very affordable smaller cities or rural areas. In most major cities, $500 won't cover a private unit, but sharing with 2–3 roommates is very manageable at that budget. Do you have a city in mind or are you flexible on location?"}
        ]
    },

    # ── SAMPLE 37 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "Do I need renters insurance and why?"},
            {"role": "assistant", "content": "Renters insurance is highly recommended and often required by landlords. Here's why: 1) It covers your personal belongings in case of theft, fire, or water damage, 2) It includes liability coverage if someone gets injured in your unit, 3) It's very affordable — typically $15–$30/month, 4) Your landlord's insurance only covers the building structure, not your personal items. For just a few dollars a month, it provides significant peace of mind. Many landlords now require proof of renters insurance before lease signing."}
        ]
    },

    # ── SAMPLE 38 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want to live near the city center but quiet. Is that possible?"},
            {"role": "assistant", "content": "Yes, it's possible with the right approach! Look for: upper-floor units in city-center buildings (street noise is reduced significantly above the 5th floor), interior-facing apartments that don't face main roads, buildings on residential side streets rather than main boulevards, and high-quality buildings with good soundproofing. Areas just 1–2 blocks off the main commercial strip are often much quieter while still offering city-center convenience. What city are you targeting?"}
        ]
    },

    # ── SAMPLE 39 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm married with a $3500/month combined budget. We want something spacious with parking."},
            {"role": "assistant", "content": "With $3,500/month combined, you have very good options! A 2-bedroom apartment or condo with parking in most cities, or a full house in mid-tier cities like Nashville, Charlotte, or Denver. Look for: included covered or garage parking (saves $100–$200/month), 1,000–1,400 sq ft which gives good spaciousness for two, and neighborhoods with a mix of amenities. Would you prefer staying urban or are you open to a quieter suburban setting?"}
        ]
    },

    # ── SAMPLE 40 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What is a duplex and is it a good rental option?"},
            {"role": "assistant", "content": "A duplex is a single building divided into two separate living units, each with its own entrance. It's like having the privacy of a house but in a more affordable two-unit structure. Pros: more space than a typical apartment, often includes a yard, more privacy than a multi-unit building, and sometimes cheaper. Cons: you share a wall with one neighbor, and the landlord may live in the other unit. They're a great option for people wanting house-like living at a lower price point."}
        ]
    },

    # ── SAMPLE 41 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 38-year-old male, in a relationship, hybrid worker. I need a home office space."},
            {"role": "assistant", "content": "For a hybrid worker who needs a dedicated home office, a 2-bedroom apartment or condo works great — use the second bedroom as your office. Look for: good natural lighting, fast internet (check if fiber is available in the building), and a quiet building with soundproofing. If you and your partner both work from home on overlap days, a 3-bedroom or a spacious 2-bedroom with a den is ideal. Would you like tips on setting up an ergonomic home office in a rental?"}
        ]
    },

    # ── SAMPLE 42 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What's the average rent for a 2-bedroom apartment in the US?"},
            {"role": "assistant", "content": "As of recent data, the national average rent for a 2-bedroom apartment in the US is approximately $1,700–$2,200/month, but this varies dramatically by city. In New York or San Francisco, a 2-bedroom can run $3,500–$6,000+. In cities like Indianapolis, Memphis, or Oklahoma City, the same size unit might be $900–$1,300. Location within a city also matters — urban cores are pricier than suburbs. Always research the specific city and neighborhood you're targeting for accurate figures."}
        ]
    },

    # ── SAMPLE 43 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 68, female, and want to be near family and medical facilities."},
            {"role": "assistant", "content": "Proximity to family and healthcare is a wonderful priority for this stage of life. I'd suggest looking for a 1-bedroom apartment or a small house within 15–20 minutes of your family, ideally in a neighborhood with a hospital or medical center nearby. Senior living communities and 55+ apartment complexes often have medical transport services built in. Amenities like an elevator in the building and ground-floor access become more important at this stage too. What city or region are your family members in?"}
        ]
    },

    # ── SAMPLE 44 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 26-year-old graphic designer. I want a space that inspires creativity."},
            {"role": "assistant", "content": "Creatives thrive in spaces with great natural light, interesting architecture, and an inspiring neighborhood. Consider: loft apartments with high ceilings and large windows, units in arts districts or creative neighborhoods, older buildings with character over cookie-cutter modern complexes, and areas near galleries, studios, or cafes. Cities like Portland, Nashville, Austin, and Denver have vibrant creative communities. A space with an extra room or nook for your design setup would be a big productivity boost."}
        ]
    },

    # ── SAMPLE 45 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "How do I negotiate rent with a landlord?"},
            {"role": "assistant", "content": "Rent negotiation is more common than most renters think! Here are tips: 1) Research comparable rents in the area to know market value, 2) Offer something in return — a longer lease, earlier move-in, or larger deposit, 3) Apply during off-peak season (winter months tend to be better for renters), 4) Highlight strong credit and stable income, 5) Ask about move-in specials like a free first month, 6) Be polite and professional — frame it as wanting to commit long-term. Even $50–$100 off per month saves $600–$1,200 a year!"}
        ]
    },

    # ── SAMPLE 46 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 31, a doctor earning over $150K. I want a luxury apartment near the hospital."},
            {"role": "assistant", "content": "With your income and proximity needs, you're looking at the premium end of the rental market near a medical district. Look for luxury high-rise apartments or upscale condos within a 10–15 minute commute to your hospital. Expect to find: concierge services, rooftop amenities, secure parking, and high-end finishes. Many hospital-adjacent neighborhoods in cities like Houston, Boston, or Chicago have premium apartment buildings catering to medical professionals. Would you like tips on what to look for in a luxury lease agreement?"}
        ]
    },

    # ── SAMPLE 47 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What does 'utilities included' mean in a rental listing?"},
            {"role": "assistant", "content": "'Utilities included' means certain or all utility costs are covered by the landlord within your rent price. This commonly includes water, trash, and sometimes heat. Some listings include electricity and internet too. Always ask the landlord to specify exactly which utilities are included — don't assume. A unit with all utilities included is worth paying slightly more for, as it simplifies budgeting. A typical utilities bundle can add $100–$250/month in value, so factor that into your comparison."}
        ]
    },

    # ── SAMPLE 48 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 22 and just graduated. Should I get a roommate or live alone?"},
            {"role": "assistant", "content": "Both have merits depending on your priorities. Living with a roommate: cuts rent by 30–50%, built-in social connection, great for recent grads entering city life on entry-level salaries. Living alone: complete privacy and independence, ideal if you value solitude or work from home, but requires a higher income (aim for 30% rule). At 22 with a first job, a roommate is usually the financially smarter move and can also be a great social experience. You can always transition to solo living after a year or two when your savings grow!"}
        ]
    },

    # ── SAMPLE 49 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm looking for a place under $1200 that accepts large dogs."},
            {"role": "assistant", "content": "Finding a large-dog-friendly place under $1,200 is definitely possible in mid-size cities. Key tips: 1) Search specifically on sites like Zillow or Apartments.com with 'pets allowed' filter and specify 'large dogs', 2) Target houses and ground-floor units — more likely to be large-dog friendly, 3) Mid-size cities like Columbus, Memphis, Louisville, or San Antonio will have the most options at this price, 4) Expect a one-time pet fee or monthly pet rent, 5) Have your dog's vaccination records and a pet resume ready. Would you like a list of the most dog-friendly cities in the US?"}
        ]
    },

    # ── SAMPLE 50 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 48, a police officer. I want a safe neighborhood for my family of 3."},
            {"role": "assistant", "content": "Given your profession, you likely have a sharp eye for what makes a neighborhood safe. For your family of 3, look for: suburban neighborhoods with low crime rates, good street lighting and sidewalks, active neighborhood watch programs, and proximity to schools. A 3-bedroom house or townhouse with a yard would give your family plenty of space. Cities like Columbus OH, Naperville IL, and Plano TX consistently rank among the safest mid-size cities in the US. Would you like help identifying safe neighborhoods in a specific city?"}
        ]
    },

    # ── SAMPLE 51 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 23 and want to live in the heart of the city with a vibrant nightlife nearby."},
            {"role": "assistant", "content": "Living in a city center near nightlife at 23 is a classic and exciting choice! Target: apartment buildings in entertainment districts or near downtown areas, studios or 1-bedrooms (you don't need much space at this stage), buildings with rooftop access for socializing, and units above the 3rd floor to balance street energy with livable noise levels. Cities like Nashville, Austin, Miami, and Chicago's River North or Wicker Park areas are legendary for young adult nightlife culture. What city or vibe interests you most?"}
        ]
    },

    # ── SAMPLE 52 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I care about sustainability. Are there eco-friendly rental options?"},
            {"role": "assistant", "content": "Eco-conscious renters have more options than ever! Look for: buildings with LEED or Energy Star certifications, units with solar panels, energy-efficient appliances, or EV charging, neighborhoods with strong walkability and bike infrastructure to reduce car use, and landlords who allow or encourage recycling and composting. Cities like Portland, Seattle, Denver, and San Francisco lead the way in green living infrastructure. Some rental platforms now have sustainability filters. Would you like tips on reducing your environmental footprint within any type of rental?"}
        ]
    },

    # ── SAMPLE 53 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 44, divorced, with one child who visits on weekends."},
            {"role": "assistant", "content": "A 2-bedroom apartment or condo would work perfectly for your situation. You get your private space plus a comfortable room for your child on visits. Look for: safe family-friendly neighborhoods, proximity to parks and schools (for your child's visits), in-unit laundry for convenience, and a welcoming community feel. You don't need a large space day-to-day, but the second bedroom makes a significant difference in quality time with your child. What city or area are you looking in?"}
        ]
    },

    # ── SAMPLE 54 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What are the most important things to check in a lease before signing?"},
            {"role": "assistant", "content": "Always review these key items before signing a lease: 1) Rent amount and due date, 2) Lease duration and renewal terms, 3) Security deposit amount and refund conditions, 4) Pet policy, 5) Guest and subletting policies, 6) Maintenance responsibilities (who handles what), 7) Early termination clauses and penalties, 8) Utilities — what's included vs what you pay, 9) Rent increase policy, 10) Rules on alterations (painting, hanging items). If anything seems unclear or unfair, ask for clarification or request a modification before signing. Never sign a lease you haven't fully read."}
        ]
    },

    # ── SAMPLE 55 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want a place with strong community feel. Any suggestions?"},
            {"role": "assistant", "content": "Great priority! For community feel, look for: townhouse communities or small apartment buildings where neighbors interact naturally, buildings with shared amenities like a courtyard, rooftop, or community room, co-living spaces which are explicitly designed for connection, and neighborhoods with active community boards, local events, or farmers markets. Mid-size cities and college towns often have the strongest neighborhood communities. Avoid large anonymous high-rise buildings if community matters to you — smaller buildings of 10–30 units are ideal."}
        ]
    },

    # ── SAMPLE 56 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I have a master's degree and earn $80K. I want a professional, clean neighborhood."},
            {"role": "assistant", "content": "At $80K you can comfortably target $1,600–$2,000/month on rent while maintaining healthy savings. Look for: well-maintained apartment buildings or condos in established neighborhoods, areas with good walkability, coffee shops, restaurants, and professional services nearby, and buildings managed by reputable property management companies. Neighborhoods known for young professionals — like Midtown in various cities, or Near North in Chicago — tend to be clean, well-maintained, and socially engaged. Any specific city in mind?"}
        ]
    },

    # ── SAMPLE 57 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 70 and need accessibility features. What should I look for in a rental?"},
            {"role": "assistant", "content": "Accessibility is critical for comfortable and safe aging. Key features to look for: ground-floor unit or building with elevators, step-free entrances and wide doorways (ADA compliant), grab bars in the bathroom or the ability to install them, a walk-in shower rather than a tub, lever-style door handles, good lighting throughout, and proximity to grocery stores and pharmacies. Senior apartment complexes and 55+ communities are often specifically designed with these features. Would you like tips on what to look for in a property walkthrough?"}
        ]
    },

    # ── SAMPLE 58 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 36 and work on-site at a factory. I want something affordable close to work."},
            {"role": "assistant", "content": "For on-site workers, minimizing commute time saves money and energy. Look for: rentals within 5–10 miles of your work site, areas near industrial or manufacturing zones which often have affordable housing nearby, a used car-friendly neighborhood with parking included, and a comfortable but simple 1–2 bedroom apartment or shared house. Proximity to work often matters more than amenities at this stage. Do you know the area around your workplace? I can give more specific neighborhood tips."}
        ]
    },

    # ── SAMPLE 59 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What's the process to apply for a rental apartment?"},
            {"role": "assistant", "content": "Here's the typical rental application process: 1) Find listings online (Zillow, Apartments.com, Craigslist), 2) Schedule a tour, 3) Submit an application (usually a form + fee of $25–$75), 4) Provide documents: photo ID, proof of income (pay stubs or bank statements), employment letter, 5) Consent to a credit and background check, 6) Provide 1–2 references (personal or professional), 7) If approved, pay security deposit and first month's rent, 8) Sign the lease, 9) Get keys and do a move-in inspection. The whole process takes 3–7 days typically."}
        ]
    },

    # ── SAMPLE 60 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 25, female, a social worker earning $35K. Where can I find affordable but decent housing?"},
            {"role": "assistant", "content": "Social workers do incredibly important work and deserve a comfortable home! At $35K, aim for $700–$875/month in rent. The best options: a room in a shared house in the city, a studio in a mid-size affordable city, or income-qualified housing programs (many cities have workforce housing initiatives for essential workers). Cities like Pittsburgh, Louisville, Indianapolis, and Albuquerque offer decent quality housing in your range. Some nonprofits also assist social service workers with affordable housing resources. Would you like information on housing assistance programs?"}
        ]
    },

    # ── SAMPLE 61 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I travel frequently for work. What rental setup makes the most sense?"},
            {"role": "assistant", "content": "Frequent travelers need maximum flexibility. Best options: a furnished apartment with a month-to-month or annual lease (you keep your home base while traveling), a co-living space where management handles everything and you can sometimes pause or reduce rent while away, or a serviced apartment that feels hotel-like with minimal maintenance. Having all utilities and internet included is very helpful so you're not paying for services you're not using. How many months a year are you typically traveling?"}
        ]
    },

    # ── SAMPLE 62 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 52, male, in good health, and want to be near outdoor activities and hiking."},
            {"role": "assistant", "content": "An active lifestyle at 52 is fantastic! Cities closest to excellent outdoor and hiking opportunities include Denver CO, Boulder CO, Portland OR, Seattle WA, Asheville NC, and Salt Lake City UT. Look for neighborhoods with trailhead access, parks, or nature reserves nearby. A house with a garage to store gear, or a ground-floor apartment with easy outdoor access, would suit your lifestyle well. Do you prefer a true outdoor city or would you like to be close to a metro area too?"}
        ]
    },

    # ── SAMPLE 63 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "Can I break a lease early? What are the consequences?"},
            {"role": "assistant", "content": "Breaking a lease early is possible but usually comes with penalties. Common consequences: 1) You may owe the remaining rent until the unit is re-rented (could be months), 2) You may lose your security deposit, 3) It can negatively affect your rental history and credit score, 4) Some states allow fee-based early termination (e.g., 2 months rent), which is cleaner. Valid reasons to break a lease without penalty include military deployment, domestic violence, landlord-violating habitability standards, or job relocation in some states. Always review your lease's early termination clause first."}
        ]
    },

    # ── SAMPLE 64 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I have a poor credit score. Can I still rent an apartment?"},
            {"role": "assistant", "content": "Yes! A low credit score makes it harder but not impossible. Strategies that work: 1) Offer a larger security deposit (2–3 months), 2) Get a co-signer with good credit, 3) Provide proof of strong current income, 4) Apply to private landlords who are more flexible than large management companies, 5) Get reference letters from previous landlords, 6) Look for 'no credit check' rentals on platforms like Facebook Marketplace or local ads, 7) Room-sharing situations often don't require formal credit checks. Also, start improving your score now — even 6 months of on-time payments can help significantly."}
        ]
    },

    # ── SAMPLE 65 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 29, a chef, working late nights. I need somewhere to decompress after shifts."},
            {"role": "assistant", "content": "Chefs have a demanding lifestyle that deserves a truly restful home. I'd recommend: a quiet apartment away from nightlife noise (ironic but important for sleep!), a place with a proper kitchen since you love cooking, good blackout curtains or thick drapes for daytime sleeping, and ideally close to where you work to minimize your commute after a tiring shift. A 1-bedroom with a real kitchen and bath for decompressing is ideal — not just a studio. What neighborhood or city are you working in?"}
        ]
    },

    # ── SAMPLE 66 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm non-binary, 27, and looking for an inclusive and welcoming neighborhood."},
            {"role": "assistant", "content": "Finding an affirming community is so important! Cities and neighborhoods known for LGBTQ+ inclusivity include: Capitol Hill in Seattle, The Castro in San Francisco, Midtown in Atlanta, Boystown in Chicago, Montrose in Houston, and Hillcrest in San Diego. Beyond LGBTQ+ specific districts, most major US cities have inclusive neighborhoods. Look for buildings managed by companies with explicit non-discrimination policies. Online communities like Queer Housing Network can also help find affirming landlords and roommates. Would you like suggestions for a specific city?"}
        ]
    },

    # ── SAMPLE 67 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I earn $100K but want to save aggressively. Should I get a cheaper place?"},
            {"role": "assistant", "content": "Smart thinking! The FIRE (Financial Independence, Retire Early) and aggressive saving communities often recommend keeping housing at 15–20% of income rather than the standard 30%. At $100K, that's $1,250–$1,667/month. This is totally achievable in most US cities for a 1-bedroom or even a comfortable 2-bedroom. Living below your means in housing has one of the highest long-term financial returns — the gap goes directly into investments. Would you like suggestions for affordable but quality rentals in your target city?"}
        ]
    },

    # ── SAMPLE 68 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What's the difference between renting from a private landlord vs a property management company?"},
            {"role": "assistant", "content": "Great question! Private landlord: more personal relationship, often more flexible on pets/lease terms/negotiations, may respond faster or slower depending on the person, smaller properties. Property management company: more standardized and professional processes, clearer rules and lease terms, dedicated maintenance team, less flexibility but more accountability, usually manages larger buildings. Private landlords are great for flexibility; management companies are great for reliability and professionalism. For first-time renters, a management company's structured process can feel safer."}
        ]
    },

    # ── SAMPLE 69 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 34, a project manager. My biggest concern is proximity to public transport."},
            {"role": "assistant", "content": "Excellent priority! Living near transit saves you 1–2 hours daily, reduces stress, and can save $500–$1,000/month on car costs. Top transit-friendly cities: New York (subway), Chicago (L train), Washington DC (Metro), Boston (MBTA), San Francisco (BART/Muni), Seattle (Link Light Rail). Look for apartments within 0.25 miles of a transit stop. Many listings now show transit scores. A 1-2 bedroom apartment near a transit hub in these cities will also tend to hold its value well. Would you like recommendations for a specific city?"}
        ]
    },

    # ── SAMPLE 70 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 20-year-old student who wants to live on campus or nearby. Any advice?"},
            {"role": "assistant", "content": "Living near campus as a student is a smart choice for both cost and convenience! Options: 1) On-campus dorms — most convenient, all-inclusive, great social life, 2) Off-campus apartments within walking distance — more freedom, often cheaper per month but you manage utilities, 3) Rooms in shared houses near campus — usually the most affordable option. For off-campus, look 1–3 blocks from campus for best balance of price and convenience. Websites like Apartment List, Zillow, and your university's off-campus housing board are great starting points."}
        ]
    },

    # ── SAMPLE 71 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 41, a physical therapist. I want storage space for medical equipment."},
            {"role": "assistant", "content": "Storage space is definitely something to prioritize! Look for: apartments or condos with in-unit storage closets, basement or on-site storage units available for rent, houses or ground-floor units with a garage or utility room, and buildings that allow you to bring in bulky items via a freight elevator. Some larger 2-bedroom units have a dedicated equipment room or a walk-in closet that could double as storage. When touring, always measure doorways and elevators for large equipment transport. Would you like to know what storage unit costs to expect alongside rent?"}
        ]
    },

    # ── SAMPLE 72 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 59, widowed, prefer unfurnished. I've been renting for 30 years. Any new trends I should know?"},
            {"role": "assistant", "content": "Welcome back to the market after a long time! A few things have changed: 1) Online applications and digital lease signing are now standard, 2) Virtual tours are available for remote viewing, 3) Smart home features (keyless entry, smart thermostats) are common in newer buildings, 4) Renters insurance is increasingly required, 5) Background and credit checks are now digital and fast, 6) Short-term rental platforms have reduced availability of long-term furnished units, 7) Rent prices have risen significantly in most cities since 2020 — budget accordingly. Your 30 years of experience is a huge asset when reading leases!"}
        ]
    },

    # ── SAMPLE 73 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 32, an architect. Aesthetics and design quality of the space really matter to me."},
            {"role": "assistant", "content": "As an architect, you have a refined eye that most landlords aren't used to! Look for: pre-war or mid-century buildings with authentic character and quality materials, loft-style apartments with exposed brick, concrete, or wood, newer boutique developments by design-focused developers, and neighborhoods with architectural heritage. Avoid generic cookie-cutter apartment complexes. Cities like Chicago, New York, Boston, New Orleans, and San Francisco have exceptional architectural stock. You may also be more willing than average to negotiate for renovations — some landlords appreciate a tenant with design skills!"}
        ]
    },

    # ── SAMPLE 74 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "We are 4 college friends looking to share a 4-bedroom house."},
            {"role": "assistant", "content": "A group of 4 sharing a house is a classic and cost-effective arrangement! Key tips: 1) All roommates should be on the lease so responsibility is shared equally, 2) Create a roommate agreement covering chores, guests, noise, and shared expenses, 3) Look for houses with 2+ bathrooms to avoid morning rush conflicts, 4) A shared common space (living room + kitchen) that's spacious will prevent friction, 5) Clarify the landlord's stance on multiple tenants, 6) Use apps like Splitwise to manage shared expenses easily. What city or university town are you looking in?"}
        ]
    },

    # ── SAMPLE 75 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 47, an accountant. I want a home office, quiet environment, and a 2-year lease."},
            {"role": "assistant", "content": "You've got very clear and sensible priorities! A 2-bedroom apartment or condo in a quiet suburban neighborhood is the perfect match. Use the second bedroom as your dedicated office — tax deductible if you work from home for self-employment. A 2-year lease is a great value move: you lock in current rent rates and signal long-term commitment to landlords, which can help in negotiations. Look for buildings with soundproofing and good insulation. Fiber internet is non-negotiable for an accountant working from home. What area are you targeting?"}
        ]
    },

    # ── SAMPLE 76 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 28 and looking for something in the $1200–$1800 range. What are my options?"},
            {"role": "assistant", "content": "The $1,200–$1,800 range is a sweet spot that opens up a lot of options in most US cities! You could get: a 1-bedroom apartment in a major city like Seattle, Denver, Austin, or Atlanta; a 2-bedroom apartment in mid-size cities like Columbus, Raleigh, or Nashville; a furnished studio in an upscale building; or even a small house in suburban areas of mid-size cities. This budget gives you room to prioritize amenities like in-unit laundry, gym access, or covered parking without breaking the bank. What city are you focusing on?"}
        ]
    },

    # ── SAMPLE 77 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 53, a business analyst with a $120K salary. I want an upscale but practical home."},
            {"role": "assistant", "content": "At $120K, you can comfortably budget $2,500–$3,000/month for a premium but practical rental. I'd recommend: a spacious 2-bedroom condo or upscale apartment with high-end finishes, in-building amenities (gym, parking), and in a well-established neighborhood. 'Practical upscale' means prioritizing quality of build, noise insulation, storage, and building management over pure flash. Cities like Denver, Nashville, Charlotte, and Austin offer excellent high-quality rentals in your range without the extreme costs of NY or SF. Would you prefer urban or suburban living?"}
        ]
    },

    # ── SAMPLE 78 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 26, a journalist. Fast internet and a dedicated workspace are my must-haves."},
            {"role": "assistant", "content": "As a journalist, your workspace and internet are your lifelines! Must-checks: 1) Confirm fiber internet availability in the building (ask for actual speed, not 'high-speed' marketing), 2) A 2-bedroom or 1-bedroom with a den gives you a real desk setup, 3) Look for quiet neighborhoods or upper floors for focus, 4) A coffee shop-dense neighborhood nearby for when you need a change of scene is a bonus. Co-living spaces designed for digital workers also often include high-speed internet as a core feature. What type of journalism do you do — remote or field-based?"}
        ]
    },

    # ── SAMPLE 79 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 39, a marketing manager with a hybrid schedule. I want the best of both worlds."},
            {"role": "assistant", "content": "Hybrid workers truly have the best setup for housing — you can live slightly further from work and still commute a few times a week. Look for: a 2-bedroom apartment or condo with a dedicated home office space, in a neighborhood 20–30 minutes from your office by transit or car, with good walkability for non-work days, and strong internet. This lets you access suburban peace without sacrificing city connection. Would you like to tell me your target city? I can point you to specific neighborhoods that match this hybrid lifestyle well."}
        ]
    },

    # ── SAMPLE 80 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 31, a single dad with a 5-year-old. What should I prioritize in a rental?"},
            {"role": "assistant", "content": "Being a single parent takes real dedication — here's what to prioritize: 1) Safety above all — low crime area, secure building, good lighting, 2) Proximity to a good elementary school or daycare, 3) A 2-bedroom so your child has their own space, 4) In-unit laundry to save time on errands, 5) Proximity to a park for your child's outdoor time, 6) A responsive landlord for maintenance issues (kids create more wear and tear!). Mid-size suburban cities often hit all of these marks at a reasonable price. What's your budget range?"}
        ]
    },

    # ── SAMPLE 81 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want to move somewhere with a lower cost of living. What cities should I consider?"},
            {"role": "assistant", "content": "Great move! Here are US cities with notably lower costs of living that still offer good quality of life: Oklahoma City OK, Memphis TN, Indianapolis IN, Columbus OH, Louisville KY, Tulsa OK, Albuquerque NM, El Paso TX, San Antonio TX, and Wichita KS. These cities offer median 1-bedroom rents of $700–$1,100, good job markets in specific sectors, and strong community vibes. Compared to NY, SF, or LA, you can stretch your dollar 2–3x. What's most important to you — job market, climate, culture, or a combination?"}
        ]
    },

    # ── SAMPLE 82 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 23, a pharmacy tech. I want something clean, close to work, affordable, no frills."},
            {"role": "assistant", "content": "No frills, practical, and close to work — a perfectly sensible approach! A studio or 1-bedroom apartment near your pharmacy in a safe but simple neighborhood is exactly what you need. Aim for 30% or less of your income on rent and keep extras like gym or rooftop optional. Look for: clean, well-managed buildings, close to a grocery store and transit, quiet and functional layout. Many pharmacy technicians work rotating shifts, so blackout curtains and a quiet environment are worth prioritizing even in a 'no frills' setup. What area or city are you in?"}
        ]
    },

    # ── SAMPLE 83 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 45, a librarian. I want a cozy, bookshelf-friendly apartment."},
            {"role": "assistant", "content": "A librarian's home with extensive bookshelves is a beautiful thing! Look for: older apartments with thick plaster walls (can hold heavy shelf anchors better than drywall), high ceilings and wide walls, ground-floor or low-floor units (fewer concerns about floor weight load), a landlord willing to allow wall anchors or built-ins, and a reading nook or bay window as a bonus. Older pre-war buildings in cities like New York, Boston, Chicago, and Philadelphia are treasure troves for readers. Any idea what size apartment you need to house your collection?"}
        ]
    },

    # ── SAMPLE 84 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What rental option makes the most sense for an international student?"},
            {"role": "assistant", "content": "International students face unique rental challenges. Best options: 1) University-managed housing — easiest, no need for US credit history, all-inclusive, 2) Off-campus shared apartments — more affordable, greater independence, 3) Student housing operators like EdR or Greystar cater specifically to students with flexible requirements. Key tips: get a co-signer (a friend, professor, or university guarantee), offer to pay 2–3 months upfront if you lack a US credit history, join your university's off-campus housing Facebook group, and connect with fellow international students for roommate arrangements. What university city are you heading to?"}
        ]
    },

    # ── SAMPLE 85 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 37, a veterinarian with three cats and a small dog."},
            {"role": "assistant", "content": "As a vet, you know better than anyone how important the right space is for your animals! With multiple pets, focus on: listings that explicitly allow multiple pets (not just 'pet-friendly' which may have a 1-pet limit), houses or ground-floor units with outdoor access, hard-surface flooring like hardwood or tile (much easier to maintain with 4 pets), good ventilation to manage pet odors, and a landlord who respects your professional background with animals. Expect higher pet deposits with a multi-pet household — having your vet credentials and pet health records ready can help reassure landlords."}
        ]
    },

    # ── SAMPLE 86 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 42, going back to school for a PhD. Income will drop significantly. Advice?"},
            {"role": "assistant", "content": "Returning to school is a big and exciting decision! For managing reduced income: 1) Look into graduate student housing offered by most universities — often subsidized and convenient, 2) Consider a room in a shared house with other grad students — great social network and very affordable, 3) Some universities have family housing for older returning students, 4) Check if your program comes with a stipend that covers basic housing, 5) Downsize from your current place before starting to build a cushion, 6) Proximity to campus saves transit costs. What university and program are you considering?"}
        ]
    },

    # ── SAMPLE 87 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I prefer suburban living. What type of properties are common in suburbs?"},
            {"role": "assistant", "content": "Suburban areas offer the widest variety of rental property types. Most common: single-family houses (3–4 bedrooms, yard, garage — the quintessential suburban rental), townhouses and duplexes (great balance of space and price), and garden-style apartment complexes (2–3 story, outdoor courtyards, parking lots). Suburbs offer more square footage per dollar than urban areas, more parking, quieter streets, and better school districts. The tradeoff is car dependency and longer commutes. Do you have a specific suburban area or city region in mind?"}
        ]
    },

    # ── SAMPLE 88 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 66 and have a fixed income from social security. How do I find affordable housing?"},
            {"role": "assistant", "content": "There are specific programs designed to help seniors on fixed incomes: 1) HUD Section 8 Housing Choice Voucher — subsidizes rent based on income, 2) HUD Section 202 Supportive Housing for the Elderly — dedicated senior housing, 3) Low-Income Housing Tax Credit (LIHTC) properties — privately managed but rent-capped, 4) Area Agency on Aging — can connect you with local resources, 5) Senior-specific apartment communities often have rent structures suited to fixed incomes. The waitlists for some programs can be long, so apply early. Would you like help finding the right program for your situation?"}
        ]
    },

    # ── SAMPLE 89 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 35, a fitness trainer. I need a gym on-site or nearby. What should I look for?"},
            {"role": "assistant", "content": "As a fitness trainer, your gym situation is extra important! Options: 1) Luxury apartment buildings in most cities include well-equipped fitness centers — often 24/7 access, 2) If the in-building gym is basic (which they often are), look for a building within walking distance to a quality commercial gym, 3) Some trainers prefer to work at their client's gym, so transit accessibility may matter more than on-site equipment, 4) A unit with space for personal equipment (kettlebells, resistance bands) is a bonus. Do you need the gym for personal use, client training sessions, or both?"}
        ]
    },

    # ── SAMPLE 90 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 49, a real estate agent. I know the market well but want advice on renting vs buying."},
            {"role": "assistant", "content": "As a real estate agent you know the numbers better than most! The rent vs buy decision often hinges on: the price-to-rent ratio (if annual rent > 5% of purchase price, renting may make sense), your expected stay (break-even is typically 4–7 years in most markets), current mortgage rates (high rates shift math toward renting), and opportunity cost of the down payment. In today's rate environment (2024–2025), many markets favor renting for flexibility. Your insider knowledge of local inventory is your biggest advantage. What market are you in and what's your timeline horizon?"}
        ]
    },

    # ── SAMPLE 91 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 19, in a relationship, and we want to rent our first place together."},
            {"role": "assistant", "content": "Exciting milestone! A few pieces of practical advice for your first shared place: 1) Both of you should be on the lease for legal protection, 2) Have an honest money conversation upfront — who pays what, how you split bills, 3) A 1-bedroom or studio is the most affordable starting point for two, 4) A 2-bedroom gives you personal space which is healthy in a new cohabitation, 5) Create a simple roommate agreement even for a couple — it prevents future friction, 6) Start with a 6-month or 1-year lease before committing to longer. What city and budget are you working with?"}
        ]
    },

    # ── SAMPLE 92 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm allergic to mold and need a very dry, well-ventilated apartment."},
            {"role": "assistant", "content": "Mold allergies are serious and should absolutely guide your rental search! Red flags to avoid: basement or ground-floor units with limited sun exposure, older buildings in humid climates with poor insulation, units near rivers or in flood-prone areas, and any visible discoloration on walls or ceilings during a tour. Green flags to look for: upper floors with good cross-ventilation and natural light, newer constructions with modern HVAC and moisture barriers, dry climates like Arizona, Colorado, or Nevada, and buildings with dehumidifiers or good air exchange systems. Always check for moisture smell and ask about the building's water damage history."}
        ]
    },

    # ── SAMPLE 93 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 31-year-old male data analyst. I want to live somewhere walkable with cafes and culture."},
            {"role": "assistant", "content": "You're looking for a high walk score neighborhood! Check Walk Score (walkscore.com) to evaluate specific addresses — aim for 85+ for a truly walkable experience. Neighborhoods like Capitol Hill (Seattle), Logan Square (Chicago), Brooklyn (NYC), East Nashville, or the Short North (Columbus) are beloved by young professionals for their walkability, independent cafes, galleries, and vibrant culture. A 1-bedroom or studio apartment in these neighborhoods positions you perfectly. Would you like a walkable neighborhood recommendation for a specific city?"}
        ]
    },

    # ── SAMPLE 94 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 55, a financial advisor. I want a prestigious address that signals success."},
            {"role": "assistant", "content": "A prestigious address is a legitimate professional tool for a financial advisor! Think: upscale neighborhoods in major metros — the Upper East Side or Tribeca in NYC, Gold Coast in Chicago, Back Bay in Boston, Nob Hill in San Francisco, or Highland Park in Dallas. A well-maintained luxury building with a respected address signals credibility to clients. Consider: a spacious 2-bedroom condo with a professional lobby and good infrastructure. Some advisors also look for units that can double as a discreet client meeting space. What city are you operating in?"}
        ]
    },

    # ── SAMPLE 95 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I want to understand what HOA fees are and how they affect my rental."},
            {"role": "assistant", "content": "HOA (Homeowners Association) fees are monthly or annual charges that cover shared expenses in a community — things like maintaining common areas, building exterior, gym, pool, and lobby. As a renter in a condo or townhouse community, the HOA fee is typically the landlord's responsibility, not yours. However, landlords often build it into your rent price. Sometimes an HOA's rules also apply to tenants — like no loud music, parking rules, or pet restrictions. Always ask your landlord if the unit is in an HOA community and what rules apply to you as a tenant."}
        ]
    },

    # ── SAMPLE 96 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 60 and in good health. I want to stay active and live somewhere that supports that."},
            {"role": "assistant", "content": "An active lifestyle at 60 is wonderful to plan for! Look for: neighborhoods with a high walkability score and bike lanes, proximity to parks, trails, fitness centers, or recreation centers, communities with group fitness classes or pool access built in, and cities with mild climates year-round for outdoor activity. Boulder CO, Scottsdale AZ, San Diego CA, and Sarasota FL consistently rank as top cities for active adults over 55. A ground-floor unit or one with elevator access gives you flexibility as needs change. Would you prefer a metro area or a smaller town with strong outdoor culture?"}
        ]
    },

    # ── SAMPLE 97 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "What is subletting and is it allowed?"},
            {"role": "assistant", "content": "Subletting means renting your apartment to another person (a subtenant) while you're still legally on the lease. It's useful if you need to travel temporarily but don't want to break your lease. However, subletting is only allowed if your lease explicitly permits it or your landlord gives written approval. Doing it without permission can result in lease termination and legal consequences. Some cities (like New York and San Francisco) have tenant-friendly subletting laws that make it easier to sublet. Always check your lease and ask your landlord before subletting. Never sublet for more than your own rent amount."}
        ]
    },

    # ── SAMPLE 98 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 28, female, earn $60K and want a nice 1-bedroom under $1500."},
            {"role": "assistant", "content": "At $60K your safe rent budget is about $1,500/month — perfect alignment! You'll find great 1-bedroom options in cities like Atlanta, Dallas, Houston, Denver, Phoenix, Charlotte, and Nashville in that range, often with amenities included. Look for: well-maintained mid-tier apartment buildings, safe neighborhoods with good walkability, and in-unit laundry if possible. Avoid sacrificing safety for size — a smaller unit in a safer neighborhood is always the better trade. Would you like more specific neighborhood recommendations for any of these cities?"}
        ]
    },

    # ── SAMPLE 99 ────────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "My partner and I both work from home. We need two separate work spaces."},
            {"role": "assistant", "content": "Dual home offices are increasingly common and totally manageable! A 3-bedroom apartment or house works perfectly — two bedrooms become dedicated offices, and the third is your shared bedroom. A 2-bedroom with an additional den or alcove can also work if budgets are tighter. Key requirements: strong internet with enough bandwidth for two simultaneous video calls, good natural light in both office spaces, and sound separation between the two workspaces (separate floors or rooms not sharing a wall is ideal). Would you like advice on configuring two home offices in a rental effectively?"}
        ]
    },

    # ── SAMPLE 100 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 43 and just moved to the US. What do I need to rent an apartment as a newcomer?"},
            {"role": "assistant", "content": "Welcome to the US! Renting as a newcomer requires a bit of preparation since you won't have a US credit history. Here's what helps: 1) Passport and visa as primary ID, 2) Employment offer letter or pay stubs as income proof, 3) Bank statements showing 3–6 months of funds, 4) Offer to pay 2–3 months rent upfront, 5) International credit reports (Experian Global or Nova Credit can translate foreign credit), 6) Company-arranged corporate housing if your employer offers it, 7) Target private landlords or smaller buildings which are more flexible. Start building US credit immediately with a secured credit card. What city are you arriving in?"}
        ]
    },

    # ── SAMPLE 101 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 30 and want a place near good restaurants and a vibrant food scene."},
            {"role": "assistant", "content": "Food lovers should look at: neighborhoods known as 'restaurant rows' or culinary districts, cities with diverse and celebrated food scenes like New York, New Orleans, Houston, Chicago, Portland, and San Francisco. Walkable urban neighborhoods near food markets, food halls, or ethnic cuisine corridors are ideal. Apps like Yelp and Google Maps let you check restaurant density around any address before you commit. A unit in a mixed-use building above restaurants gives ultimate food access. Do you have a cuisine preference or dining style that should shape your neighborhood choice?"}
        ]
    },

    # ── SAMPLE 102 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 18 and want to live alone for the first time. Is it a good idea?"},
            {"role": "assistant", "content": "Living alone at 18 is absolutely possible and can be very character-building! Things to consider: 1) Budget carefully — rent should be under 30% of your income, 2) At 18, income may be limited, so a studio or room in a shared house may be more realistic, 3) Make sure you understand all costs beyond rent: utilities, internet, groceries, renters insurance, 4) Have an emergency fund of at least 1–2 months expenses, 5) Choose a safe neighborhood especially for your first solo experience. Living alone teaches responsibility fast. Do you have a steady income source or support from family as a backup?"}
        ]
    },

    # ── SAMPLE 103 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 34, a single mom with two kids aged 8 and 11. School quality is my #1 priority."},
            {"role": "assistant", "content": "School quality for your kids is the best investment you can make in housing. Here's how to approach it: 1) Use GreatSchools.org to search rentals by school quality scores, 2) Target suburban neighborhoods in districts ranked 8–10/10, 3) A 3-bedroom house or townhouse will give both kids their own space, 4) Safety and walkability to school are secondary priorities worth checking, 5) Cities like Naperville IL, Plano TX, Irvine CA, and Carmel IN are frequently cited for outstanding public schools. Budget will guide what level of school district is attainable. What's your monthly budget and what region are you open to?"}
        ]
    },

    # ── SAMPLE 104 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm a 57-year-old male, associate's degree, earning $40K. Simple, no-fuss rental please."},
            {"role": "assistant", "content": "Straightforward and honest — I respect that! At $40K, your practical budget is around $800–$1,000/month. A clean, simple 1-bedroom apartment or a room in a well-managed shared house in a mid-size or small city is your best option. Focus on: reliable landlord/management, safe neighborhood, close to grocery stores, and functional appliances. Skip the frills — rooftop pools and concierge don't add real value to a comfortable, simple life. Cities like Indianapolis, Memphis, Louisville, and Albuquerque have solid 1-bedrooms in your range. Would you like a shortlist of cities with the best value rentals at your budget?"}
        ]
    },

    # ── SAMPLE 105 ───────────────────────────────────────────
    {
        "messages": [
            {"role": "system", "content": "You are a helpful rental assistant that recommends properties based on user preferences."},
            {"role": "user",   "content": "I'm 40, married, no kids, both working, combined income $180K. We want something premium."},
            {"role": "assistant", "content": "With a combined income of $180K and no dependents, you're positioned for a truly premium rental experience. You could comfortably budget $4,000–$5,000/month for housing. This opens up: luxury 2-bedroom condos or penthouses in top urban neighborhoods, waterfront properties in cities like Miami, Seattle, or Boston, high-end buildings with full concierge, doorman, valet parking, and resort-like amenities, or a spacious executive house in a prestigious suburb. The key question is: do you prefer the energy of urban luxury or the space and privacy of an upscale suburban home? Both are very attainable at your level."}
        ]
    },

]

# ── Quick stats ───────────────────────────────────────────────
if __name__ == "__main__":
    print(f"Total samples      : {len(dataset)}")
    print(f"Format             : OpenAI / Anthropic chat fine-tuning (messages list)")
    print(f"Roles used         : system, user, assistant")
    print(f"Topics covered     : Budget advice, property types, age/gender diversity,")
    print(f"                     pet policies, lease terms, amenities, safety, credit,")
    print(f"                     accessibility, relocations, families, students, retirees")
    print()
    print("Sample entry preview:")
    import json
    print(json.dumps(dataset[0], indent=2))
