package se.adventsapp;

public class Keypad9Digits extends Keypad {

	public Keypad9Digits() {
		this.currentKey = '5';
	}

	@Override
	public void moveCommand(String string) {
		switch (this.getCurrentKey()) {
		case '1':
			if (string.equals("R")) {
				this.currentKey = '2';
			} else if (string.equals("D")) {
				this.currentKey = '4';
			}
			break;
		case '2':
			if (string.equals("L")) {
				this.currentKey = '1';
			} else if (string.equals("D")) {
				this.currentKey = '5';
			} else if (string.equals("R")) {
				this.currentKey = '3';
			}
			break;
		case '3':
			if (string.equals("L")) {
				this.currentKey = '2';
			} else if (string.equals("D")) {
				this.currentKey = '6';
			}
			break;
		case '4':
			if (string.equals("R")) {
				this.currentKey = '5';
			} else if (string.equals("D")) {
				this.currentKey = '7';
			} else if (string.equals("U")) {
				this.currentKey = '1';
			}
			break;
		case '5':
			if (string.equals("L")) {
				this.currentKey = '4';
			} else if (string.equals("D")) {
				this.currentKey = '8';
			} else if (string.equals("R")) {
				this.currentKey = '6';
			} else if (string.equals("U")) {
				this.currentKey = '2';
			}
			break;
		case '6':
			if (string.equals("L")) {
				this.currentKey = '5';
			} else if (string.equals("D")) {
				this.currentKey = '9';
			} else if (string.equals("U")) {
				this.currentKey = '3';
			}
			break;
		case '7':
			if (string.equals("R")) {
				this.currentKey = '8';
			} else if (string.equals("U")) {
				this.currentKey = '4';
			}
			break;
		case '8':
			if (string.equals("L")) {
				this.currentKey = '7';
			} else if (string.equals("R")) {
				this.currentKey = '9';
			} else if (string.equals("U")) {
				this.currentKey = '5';
			}
			break;
		case '9':
			if (string.equals("L")) {
				this.currentKey = '8';
			} else if (string.equals("U")) {
				this.currentKey = '6';
			}
			break;

		}

	}

}
