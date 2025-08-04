from config.items import ITEMS

# Check for duplicate item names
item_names = [item.name for item in ITEMS]
unique_names = set(item_names)

print(f"Total items: {len(ITEMS)}")
print(f"Unique item names: {len(unique_names)}")

if len(item_names) != len(unique_names):
    print("\nDuplicate items found:")
    for name in unique_names:
        count = item_names.count(name)
        if count > 1:
            print(f"  '{name}' appears {count} times")
            
    # Show all item names to help identify the issue
    print(f"\nAll item names:")
    for i, name in enumerate(item_names):
        print(f"{i+1:2d}. {name}")
else:
    print("No duplicates found!")
