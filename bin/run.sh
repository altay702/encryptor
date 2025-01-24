SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"

function generate_key() {
  echo "Generating/Updating key..."
  python3 "$SCRIPTS_DIR/keygen.py"
}

function encrypt_file() {
  read -rp "Enter the path to the file you want to encrypt: " FILEPATH
  if [ -f "$FILEPATH" ]; then
    python3 "$SCRIPTS_DIR/encrypt.py" "$FILEPATH"
  else
    echo "File not found: $FILEPATH"
  fi
}

function decrypt_file() {
  read -rp "Enter the path to the encrypted file (.enc): " ENCFILE
  if [ -f "$ENCFILE" ]; then
    python3 "$SCRIPTS_DIR/decrypt.py" "$ENCFILE"
  else
    echo "File not found: $ENCFILE"
  fi
}

function main_menu() {
  while true; do
    echo "---------------------------------"
    echo "  Encryptor made by Altay702"
    echo "---------------------------------"
    echo "1) Generate or Update Key"
    echo "2) Encrypt File"
    echo "3) Decrypt File"
    echo "4) Exit"
    read -rp "Choose an option [1-4]: " CHOICE

    case "$CHOICE" in
      1) generate_key ;;
      2) encrypt_file ;;
      3) decrypt_file ;;
      4) echo "Exiting..."; exit 0 ;;
      *) echo "Invalid choice." ;;
    esac
  done
}

# Run main menu
main_menu
