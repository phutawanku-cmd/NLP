import re

def eliza_response(user_input):
    rules = [
        # กฎข้อ 1: ดักจับน้ำหนักที่ยกได้ (Personal Record)
        # รองรับทั้งคำว่า pr, hit, lifted ตามด้วยตัวเลข และหน่วย kg หรือ lbs
        (
            re.compile(r".*\b(pr|hit|lifted)\b\s+(\d+)\s*(kg|lbs)\b.*", re.IGNORECASE),
            lambda m: f"Whoa, {m.group(2)} {m.group(3)}?! That's some serious weight, bro. Make sure your form is strict!"
        ),
        
        # กฎข้อ 2: ดักจับตารางออกกำลังกาย (Push / Pull / Legs)
        (
            re.compile(r".*\b(push|pull|legs)\b.*", re.IGNORECASE),
            lambda m: f"Ah, a {m.group(1).title()} day! Keep your intensity high and train close to failure. Leave maybe 1-2 RIR (Reps in Reserve)."
        ),
        
        # กฎข้อ 3: ดักจับเป้าหมายโภชนาการ (ปริมาณโปรตีน)
        # รองรับตัวเลขที่ตามด้วยคำว่า grams หรือ g (มีหรือไม่มีเว้นวรรคก็ได้)
        (
            re.compile(r".*\bprotein.*\b(\d+)\s*(grams|g)\b.*", re.IGNORECASE),
            lambda m: f"Aiming for {m.group(1)} grams of protein is solid. Whether it's whey or plant-based isolate, just hit your daily macros to build that muscle."
        ),
        
        # กฎข้อ 4: ดักจับอาการบาดเจ็บหรือปวดกล้ามเนื้อ
        (
            re.compile(r".*\b(sore|tired|pain)\b.*", re.IGNORECASE),
            lambda m: "Listen to your body. If it's just muscle soreness (DOMS), keep moving. If it's sharp pain, take a rest day."
        )
    ]

    for pattern, response in rules:
        match = pattern.match(user_input)
        if match:
            return response(match)

    # Fallback กรณีที่ไม่ได้พิมพ์คีย์เวิร์ดใดๆ เลย
    return "Time to get those gains! What's your workout routine looking like today?"


def main():
    print("========================================")
    print("         Gym Bro & Fitness Bot          ")
    print(" Type 'quit' to exit the program        ")
    print("========================================")

    while True:
        user = input("\nYou : ")

        if user.lower() == "quit":
            print("Bot : Stay consistent. See you at the gym!")
            break

        print("Bot :", eliza_response(user))


if __name__ == "__main__":
    main()
