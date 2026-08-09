import * as kit from '@volar/kit';
import { Diagnostic, DiagnosticSeverity } from '@volar/language-server';
export { Diagnostic, DiagnosticSeverity };
export interface CheckResult {
    status: 'completed' | 'cancelled' | undefined;
    fileChecked: number;
    errors: number;
    warnings: number;
    hints: number;
    fileResult: {
        errors: kit.Diagnostic[];
        fileUrl: URL;
        fileContent: string;
        text: string;
    }[];
}
export declare class AstroCheck {
    private ts;
    linter: ReturnType<(typeof kit)['createTypeScriptChecker']>;
    private readonly workspacePath;
    private readonly typescriptPath;
    private readonly tsconfigPath;
    constructor(workspacePath: string, typescriptPath: string | undefined, tsconfigPath: string | undefined);
    /**
     * Lint a list of files or the entire project and optionally log the errors found
     * @param fileNames List of files to lint, if undefined, all files included in the project will be linted
     * @param logErrors Whether to log errors by itself. This is disabled by default.
     * @return {CheckResult} The result of the lint, including a list of errors, the file's content and its file path.
     */
    lint({ fileNames, cancel, logErrors, }: {
        fileNames?: string[] | undefined;
        cancel?: () => boolean;
        logErrors?: {
            level: 'error' | 'warning' | 'hint';
        } | undefined;
    }): Promise<CheckResult>;
    private initialize;
    /**
     * The checker is built on Volar and TypeScript's programmatic Language Service API
     * (`ts.sys`, `ts.findConfigFile`, `LanguageServiceHost`, etc.). TypeScript's native
     * compiler does not ship that API yet — `require('typescript')` only exposes `version`
     * and `versionMajorMinor` — so continuing would crash later with an opaque
     * `Cannot read properties of undefined` error. Fail early with an actionable message.
     */
    private assertCompatibleTypeScript;
    private getTsconfig;
}
