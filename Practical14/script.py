import xml.dom.minidom
import xml.sax
import datetime

# Define target namespaces for analysis
target_namespaces = ["molecular_function", "biological_process", "cellular_component"]

def print_results(method_name, results, time_taken):
    print(f"\n--- Results using {method_name} ---")
    print(f"Time taken: {time_taken}")
    for ns in target_namespaces:
        data = results[ns]
        print(f"Ontology: {ns}")
        print(f"  - Term ID with max <is_a>: {data['id']}")
        print(f"  - Number of <is_a> elements: {data['count']}")

# =================================================================
# DOM
# =================================================================
def run_dom_analysis(file_path):
    start = datetime.datetime.now()
    
    # Initialize a dictionary to store the term with the maximum <is_a> count for each namespace
    max_isa = {ns: {"id": "None", "count": 0} for ns in target_namespaces}
    
    # Parse the XML file using DOM
    dom_tree = xml.dom.minidom.parse(file_path)
    collection = dom_tree.documentElement
    terms = collection.getElementsByTagName("term")
    
    for term in terms:
        ns_elements = term.getElementsByTagName("namespace")
        if not ns_elements: continue
        ns = ns_elements[0].firstChild.nodeValue.strip()
        
        if ns in target_namespaces:
            isa_count = len(term.getElementsByTagName("is_a"))

            if isa_count > max_isa[ns]["count"]:
                term_id = term.getElementsByTagName("id")[0].firstChild.nodeValue.strip()
                max_isa[ns]["id"] = term_id
                max_isa[ns]["count"] = isa_count
                
    end = datetime.datetime.now()
    return max_isa, end - start

# =================================================================
# SAX
# =================================================================
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.results = {ns: {"id": "None", "count": 0} for ns in target_namespaces}
        self.current_tag = ""
        self.buffer = ""
        
        self.temp_id = ""
        self.temp_ns = ""
        self.temp_isa_count = 0

    def startElement(self, tag, attributes):
        self.current_tag = tag
        if tag == "term":
            self.temp_id = ""
            self.temp_ns = ""
            self.temp_isa_count = 0
        self.buffer = "" 

    def characters(self, content):
        self.buffer += content

    def endElement(self, tag):
        if tag == "id":
            self.temp_id = self.buffer.strip()
        elif tag == "namespace":
            self.temp_ns = self.buffer.strip()
        elif tag == "is_a":
            self.temp_isa_count += 1
        elif tag == "term":
            if self.temp_ns in target_namespaces:
                if self.temp_isa_count > self.results[self.temp_ns]["count"]:
                    self.results[self.temp_ns]["id"] = self.temp_id
                    self.results[self.temp_ns]["count"] = self.temp_isa_count
        
        self.current_tag = ""

def run_sax_analysis(file_path):
    start = datetime.datetime.now()
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    
    end = datetime.datetime.now()
    return handler.results, end - start

# =================================================================
# Main execution
# =================================================================
if __name__ == "__main__":
    xml_file = "go_obo.xml"
    
    try:
        # DOM analysis
        dom_res, dom_time = run_dom_analysis(xml_file)
        print_results("DOM", dom_res, dom_time)
        
        # SAX analysis
        sax_res, sax_time = run_sax_analysis(xml_file)
        print_results("SAX", sax_res, sax_time)
        
        # Compare performance
        if sax_time < dom_time:
            faster = "SAX"
        else:
            faster = "DOM"
            
        print(f"\nConclusion: {faster} was the fastest method.")

    except FileNotFoundError:
        print(f"Error: {xml_file} not found. Please check the file path.")

# COMMENT: SAX is much faster than DOM for this task because the Gene Ontology file is large. 
# SAX processes the file line-by-line (event-driven) without loading the entire 
# 100MB+ file into memory like DOM does.


