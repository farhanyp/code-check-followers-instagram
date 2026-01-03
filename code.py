import json

with open("followers_1.json", "r") as f:
    followers_data = json.load(f)

with open("following.json", "r") as f:
    following_data = json.load(f)

# Ambil semua username dari followers
followers_usernames = [item["string_list_data"][0]["value"] for item in followers_data]

# Ambil data dari following yang tidak ada di followers
not_follow_back = [
    {
        "username": item["title"],
        "href": item["string_list_data"][0]["href"]
    }
    for item in following_data["relationships_following"]
    if item["title"] not in followers_usernames
]

# Visual tampilannya
print("\n🚫  Orang yang tidak follow back kamu")
print("======================================")

if not not_follow_back:
    print("✅ Semua orang yang kamu follow sudah follow balik!\n")
else:
    for i, user in enumerate(not_follow_back, 1):
        print(f"{i:02}. @{user['username']}")
        print(f"   🔗 {user['href']}")
        print("-" * 40)

print(f"\nTotal: {len(not_follow_back)} akun yang tidak follow back.\n")
