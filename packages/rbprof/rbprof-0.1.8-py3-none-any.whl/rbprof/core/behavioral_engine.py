import json
import hashlib
from datetime import datetime
import numpy as np  

class BehaviorEngine:
    def __init__(self):
        self.crypto_apis = ["CryptEncrypt", "BCryptEncrypt"]
        self.suspicious_ips = {"185.143.223.47"}

    def analyze(self, filepath):
        """Analyze a file for ransomware behavior.
        
        Args:
            filepath (str): Path to the file to analyze.
        
        Returns:
            dict: Analysis results with consistent structure.
        """
        try:
            # Validate input
            if not isinstance(filepath, str):
                raise ValueError("filepath must be a string")
            
            # Initialize result with basic file info
            result = {
                "filename": os.path.basename(filepath),
                "filepath": filepath,
                "status": "success",
                "timestamp": str(datetime.now()),
                "analysis": {}
            }

            # Perform analysis steps
            result["analysis"]["apis"] = self._trace_apis(filepath)
            result["analysis"]["network"] = self._check_network(filepath)
            result["analysis"]["process_tree"] = self._get_process_tree(filepath)
            result["analysis"]["file_hashes"] = self._calculate_hashes(filepath)
            
            # Add risk assessment
            result["risk_score"] = self._assess_risk(result["analysis"])
            
            return result

        except Exception as e:
            # Return error structure consistent with main.py expectations
            return {
                "status": "error",
                "error": str(e),
                "filename": os.path.basename(filepath) if isinstance(filepath, str) else "unknown",
                "timestamp": str(datetime.now())
            }

    def _trace_apis(self, filepath):
        """Trace API calls (mock implementation)."""
        try:
            if "malware" in filepath.lower():
                return ["FindFirstFileW", "CryptEncrypt", "DeleteShadowCopies"]
            return []
        except:
            return []

    def _check_network(self, filepath):
        """Check network activity (mock implementation)."""
        try:
            if "malware" in filepath.lower():
                return {
                    "suspicious": True,
                    "connections": [
                        {"dst_ip": "185.143.223.47", "port": 443, "protocol": "HTTPS"}
                    ]
                }
            return {"suspicious": False, "connections": []}
        except:
            return {"suspicious": False, "connections": [], "error": "Network check failed"}

    def _get_process_tree(self, filepath):
        """Get process tree (mock implementation)."""
        try:
            if "malware" in filepath.lower():
                return ["explorer.exe → cmd.exe → vssadmin.exe"]
            return []
        except:
            return []

    def _calculate_hashes(self, filepath):
        """Calculate file hashes (mock implementation)."""
        try:
            return {
                "md5": "d41d8cd98f00b204e9800998ecf8427e",  # Mock hash
                "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
            }
        except:
            return {"error": "Hash calculation failed"}

    def _assess_risk(self, analysis_data):
        """Calculate risk score based on analysis results."""
        try:
            risk_score = 0
            if analysis_data.get("apis"):
                risk_score += 30
            if analysis_data.get("network", {}).get("suspicious"):
                risk_score += 40
            if analysis_data.get("process_tree"):
                risk_score += 30
            return min(100, risk_score)  # Cap at 100
        except:
            return 0