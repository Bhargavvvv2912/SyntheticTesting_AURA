# validation_synthetic.py
import sys
import pydantic
import pydantic_core

def run_test():
    print("--- Starting Synthetic Pydantic Smoke Test ---")
    try:
        print(f"Pydantic Version: {pydantic.__version__}")
        print(f"Pydantic Core Version: {pydantic_core.__version__}")

        # Test 1: Basic Model Definition
        print("--> Test 1: Defining a User model...")
        class User(pydantic.BaseModel):
            id: int
            name: str
        
        # Test 2: Validation Logic (Uses pydantic-core internally)
        print("--> Test 2: Validating data...")
        user = User(id=123, name="AURA Agent")
        print(f"    User created: {user}")
        
        # Test 3: Error Handling
        print("--> Test 3: Checking validation errors...")
        try:
            User(id="not-an-int", name="Fail")
        except pydantic.ValidationError as e:
            print("    Caught expected validation error.")

        print("\n--- TEST PASSED: Environment is healthy. ---")
        sys.exit(0)

    except Exception as e:
        print(f"\n--- TEST FAILED: {e} ---", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    run_test()