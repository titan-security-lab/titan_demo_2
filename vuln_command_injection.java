import java.io.*;

public class VulnerableNetwork {
    /**
     * VULNERABLE: Command Injection - CWE-78
     * Attacker can inject: 8.8.8.8; cat /etc/passwd
     */
    public String pingHost(String host) throws IOException {
        // Direct command execution with user input!
        Runtime runtime = Runtime.getRuntime();
        Process process = runtime.exec("ping -c 4 " + host);
        
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(process.getInputStream())
        );
        
        StringBuilder output = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            output.append(line).append("\n");
        }
        
        return output.toString();
    }
}
