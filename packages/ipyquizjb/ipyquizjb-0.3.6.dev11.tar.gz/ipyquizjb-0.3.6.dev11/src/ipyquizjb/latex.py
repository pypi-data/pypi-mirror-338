from IPython.display import display, HTML
import ipywidgets as widgets

def latexize(widget: widgets.DOMWidget):
    """
    Adds an HTML class to the widget that is used to tell
    MathJax to render these as math 
    """
    widget.add_class("ipyquizjb-render-math")
    return widget

def setup_latex():
    """NOTE:
    The version of MathJax seems to change when using IPython.display.HTML,
    but exactly when it happens varies, we are therefore checking the version
    before calling the corresponding typesetting function.
    """
    display(HTML("""<script>
function versionAgnosticTypeset(element) {
    if (MathJax.version.startsWith("3")) {
        if (element) {
            MathJax.typeset([element]) 
        } else {
            MathJax.typeset()
        }   
    } else {
        if (element) {
            MathJax.Hub.Queue(['Typeset', MathJax.Hub, element]);
        } else {
            MathJax.Hub.Queue(['Typeset', MathJax.Hub]);
        }   
    }
}

function make_latex_buttons_clickable() {
    for (el of document.getElementsByClassName("mjx-chtml MathJax_CHTML")) {
        el.addEventListener("click", (e) => {
            e.stopPropagation();
            var element = e.target;
            var parent = element.parentElement
            while (!parent.classList.contains("jupyter-button")) {
                parent = parent.parentElement;
            }
            console.log("clicked button")
            console.log(parent)
            parent.click();	
        }); 
    };
}
                
// Used on every rerender
function typesetAll() {
    console.log("Rerender typeset");
    for (element of document.getElementsByClassName("ipyquizjb-render-math")) {
        versionAgnosticTypeset(element);
    }
}

versionAgnosticTypeset();
</script>"""))
    

def render_latex():
    """
    TODO: Doc"""
    display(HTML("<script>typesetAll()</script>"))

    


def make_latex_buttons_clickable():
    """TODO: Doc"""
    display(HTML("""<script>
MathJax.Hub.Queue(make_latex_buttons_clickable)
</script>"""))

