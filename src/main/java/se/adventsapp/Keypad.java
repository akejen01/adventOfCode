package se.adventsapp;

import java.util.List;

public class Keypad {

	private int currentKey;

	
	public Keypad() {
		currentKey = 5;
	}
	
	public int getCurrentKey() {

		return this.currentKey;
	}

	public void moveCommand(String string) {

	
		switch (this.getCurrentKey()) {
		case 1:
			if (string.equals("R")){
				this.currentKey = 2;
			} else if(string.equals("D")){
				this.currentKey = 4;
			}
			break;
		case 2:
			if (string.equals("L")){
				this.currentKey = 1;
			} else if(string.equals("D")){
				this.currentKey = 5;
			} else if (string.equals("R")){
				this.currentKey = 3;
			}
			break;
		case 3:
			if (string.equals("L")){
				this.currentKey = 2;
			} else if(string.equals("D")){
				this.currentKey = 6;
			}
			break;
		case 4:
			if (string.equals("R")){
				this.currentKey = 5;
			} else if(string.equals("D")){
				this.currentKey = 7;				
			}else if (string.equals("U")){
				this.currentKey = 1;
			}
			break;
		case 5:
			if (string.equals("L")){
				this.currentKey = 4;
			} else if(string.equals("D")){
				this.currentKey = 8;
			} else if (string.equals("R")){
				this.currentKey = 6;
			}else if( string.equals("U")){
				this.currentKey = 2;
			}
			break;
		case 6:
			if (string.equals("L")){
				this.currentKey = 5;
			} else if(string.equals("D")){
				this.currentKey = 9;
			} else if(string.equals("U")){
				this.currentKey = 3;
			}
			break;
		case 7:
			if (string.equals("R")){
				this.currentKey = 8;
			} else if(string.equals("U")){
				this.currentKey = 4;
			}
			break;
		case 8:
			if (string.equals("L")){
				this.currentKey = 7;
			} else if(string.equals("R")){
				this.currentKey = 9;
			} else if(string.equals("U")){
				this.currentKey = 5;
			}
			break;
		case 9:
			if (string.equals("L")){
				this.currentKey = 8;
			} else if(string.equals("U")){
				this.currentKey = 6;
			}
			break;
			
		}

	}

	public void moveCommandList(List<String> commandList){
		
		for (String commandString : commandList) {
			this.moveCommand(commandString);
		}
		
	}
	
	
	public void moveCommandList(String string) {
	
		String[] listan = string.split("");
		
		System.out.println("Längd :" + listan.length);
		
		for (String commandString : listan) {
			this.moveCommand(commandString);
		}
		
	}
	
	
	
	
	
}
