import click
from .yaml_processor import process_yaml

@click.command()
@click.argument('input_file', type=click.File('r'), required=False)
@click.option('--yaml', '-y', help='YAML string to process directly')
@click.option('--output', '-o', type=click.File('w'), default='-', 
              help='Output file (default: stdout)')
def main(input_file, yaml, output):
    """Process YAML by capitalizing all string values.
    
    There are three ways to provide input:
    1. INPUT_FILE: Path to a YAML file
    2. --yaml/-y: Direct YAML string (for simple YAML)
    3. Standard input (for any YAML, including complex structures)
    
    If no input method is specified, reads from stdin.
    
    Examples:
        # Process a file:
        yaml-processor input.yaml
        
        # Process a simple YAML string:
        yaml-processor --yaml "name: test"
        
        # Process complex YAML from stdin:
        echo "name: test
        config:
          env: dev" | yaml-processor
        
        # Process and save to file:
        yaml-processor input.yaml -o output.yaml
    """
    # Determine input source
    if yaml is not None:
        yaml_content = yaml
    elif input_file is not None:
        yaml_content = input_file.read()
    else:
        yaml_content = click.get_text_stream('stdin').read()
    
    try:
        # Process the YAML
        result = process_yaml(yaml_content)
        
        # Write the result
        output.write(result)
        
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()
    except Exception as e:
        click.echo(f"Unexpected error: {str(e)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main() 