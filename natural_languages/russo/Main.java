

import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.FileInputStream;

import java.io.FileNotFoundException;
import java.io.IOException;


public class Main
{
	private static void println(String s)
	{ System.out.println(s); }

	public static void main(String[] argv)
	{
		String content = new String();
		String s = new String();
		try
		{
			BufferedReader reader = new BufferedReader(new InputStreamReader(new FileInputStream("this")));

			while(s != null)
			{
				s = reader.readLine();
				content += s + "\n";
			}

//			println(content);
		}
		catch(FileNotFoundException e)
		{ println("File nao encontrado."); }
		catch(IOException e)
		{ println(e.getMessage()); }

		s = content.replaceAll("\n", "<br />\n");
		println(s);
	}
}
