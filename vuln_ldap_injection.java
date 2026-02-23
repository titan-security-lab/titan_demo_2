import javax.naming.*;
import javax.naming.directory.*;

public class VulnerableLDAP {
    /**
     * VULNERABLE: LDAP Injection - CWE-90
     * Attacker can inject: *)(uid=*))(|(uid=*
     */
    public void searchUser(String username) throws NamingException {
        DirContext ctx = new InitialDirContext();
        
        // Direct string concatenation - LDAP injection!
        String filter = "(uid=" + username + ")";
        
        NamingEnumeration results = ctx.search(
            "ou=users,dc=example,dc=com",
            filter,
            new SearchControls()
        );
    }
}
