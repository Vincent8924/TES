
import clip
import time

def process_clipboard_content(content):
    """
    This is our "Rule Base" and "Inference Engine."
    It checks the "fact" (content) against its rules.
    """
    
    print("-" * 30)
    print(f"🕵️  New Fact to process: {content[:70]}...")

    # --- Rule Base (Knowledge Base) ---

    # Rule 1: Check for a URL
    if content.startswith('http://') or content.startswith('https://'):
        print("✅ Rule Fired: https://dictionary.cambridge.org/dictionary/english/detected")
        print("   Action: (This is where you could open a browser or save the link)")
    
    # Rule 2: Check for a keyword "error" (case-insensitive)
    elif 'error' in content.lower():
        print("🚨 Rule Fired: [Error Message Detected]")
        print("   Action: (This is where you could log this error to a file)")

    # Rule 3: Check for a possible email address (very simple check)
    elif '@' in content and '.' in content and ' ' not in content:
        print("📧 Rule Fired: [Email Address Detected]")
        print("   Action: (This is where you could add it to a contact list)")

    # Default Rule: If no other rule fires
    else:
        print("⚪ No specific rule fired. Content is just text.")
    
    print("-" * 30)


# --- Main System Loop ---

print("📋 Clipboard Expert System is RUNNING...")
print("Copy text to your clipboard to see it work.")
print("Press Ctrl+C to stop.")

# This variable handles our "Refraction"
# It stores the last fact we processed.
last_processed_content = None

try:
    # clip.spy() provides new "facts"
    for content in clip.spy():
        
        # --- Refraction Check ---
        # If the new content is the same as the last one,
        # don't process it again. This prevents loops.
        if content == last_processed_content:
            continue  # Skip, this fact was already processed.
        
        # --- Fire Rules ---
        # We have a new, unique fact. Let the
        # "inference engine" process it against the "rule base."
        process_clipboard_content(content)
        
        # --- Update Memory ---
        # Remember this content so we don't process it again
        last_processed_content = content
        
        # A small delay to prevent rapid, accidental re-copies
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 System shutting down. Goodbye!")