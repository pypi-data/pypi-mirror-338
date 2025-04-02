// Interface for the fetched page data.
export default interface UIContent {
    heading: string | null;
    content: string;
    metadata: { [key: string]: string | number | boolean };
}
